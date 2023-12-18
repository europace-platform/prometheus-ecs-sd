# prometheus-ecs-sd
ECS Service Discovery for Prometheus

Find the Europace documentation on how to use this in [shared-monitoring](https://github.com/europace-platform/shared-monitoring/blob/b9657bf2e759daea4d14b21bb1ec3b0441142024/docs/ecs%20monitoring.md)

## Deployment

Building the Container image, pushing it to ECR and deploying to as sidecar are manual steps.

1. Login to `ep-shared` AWS account. 
2. Locate ECR repository `/prom/prometheus-ecs-sd`.
3. Figure out latest version (eg. `v1.5`) and then increase by one minor. This is the new version (eg. `v1.6`).
4. Run the following commands in the root of this directory to 
    ```shell
    awsume ep-shared.Europace-PaaS-Admin
    aws ecr get-login-password --region eu-central-1 | podman login --username AWS --password-stdin 856650302511.dkr.ecr.eu-central-1.amazonaws.com
    podman build -t prom/prometheus-ecs-sd:latest .
    podman tag prom/prometheus-ecs-sd:latest 856650302511.dkr.ecr.eu-central-1.amazonaws.com/prom/prometheus-ecs-sd:v1.5
    podman push 856650302511.dkr.ecr.eu-central-1.amazonaws.com/prom/prometheus-ecs-sd:v1.5
    podman tag prom/prometheus-ecs-sd:latest 856650302511.dkr.ecr.eu-central-1.amazonaws.com/prom/prometheus-ecs-sd:latest
    podman push 856650302511.dkr.ecr.eu-central-1.amazonaws.com/prom/prometheus-ecs-sd:latest
    ```
5. Change version in Prometheus sidecars for deployment:
    - [ps.ecsDiscoveryImageVersion](https://github.com/europace/eks-services-observability/blob/88a285430d418f781997e285906cd37fd34c7cfe/cdk8s/src/namespaces/shared-monitoring/common.ts#L6)
    - [mtp.ecsDiscoveryImageVersion](https://github.com/europace/eks-services-observability/blob/88a285430d418f781997e285906cd37fd34c7cfe/cdk8s/src/namespaces/shared-monitoring/common.ts#L29)

## Info
This tool provides Prometheus service discovery for Docker containers running on AWS ECS. You can easily instrument your app using a Prometheus
client and enable discovery adding an ENV variable at the Service Task Definition. Your container will then be added
to the list of Prometheus targets to be scraped. Requires python2 or python3 and boto3. Works with Prometheus 2.x. It supports bridge, host
and awsvpc (EC2 and Fargate) network modes.

## Setup
``discoverecs.py`` should run alongside the Prometheus server. It generates targets using JSON file service discovery. It can
be started by running:

``python discoverecs.py --directory /opt/prometheus-ecs``

Where ``/opt/prometheus-ecs`` is defined in your Prometheus config as a file_sd_config job:

```YAML
- job_name: 'ecs-1m'
  scrape_interval: 1m
  file_sd_configs:
    - files:
        - /opt/prometheus-ecs/1m-tasks.json
  relabel_configs:
    - source_labels: [metrics_path]
      action: replace
      target_label: __metrics_path__
      regex: (.+)
```

You can also specify a discovery interval with ``--interval`` (in seconds). Default is 60s. We also provide caching to minimize hitting query
rate limits with the AWS ECS API. ``discoverecs.py` runs in a loop until interrupted and will output target information to stdout.

To make your application discoverable by Prometheus, you need to set the following ENV variable in your task definition:

``{"name": "PROMETHEUS", "value": "true"}``

Metric path and scrape interval is supported via PROMETHEUS_ENDPOINT:

``"interval:/metric_path,..."``

Examples:

```
"5m:/mymetrics,30s:/mymetrics2"
"/mymetrics"
"30s:/mymetrics1,/mymetrics2"
```

Under ECS task definition (task.json):

``{"name": "PROMETHEUS_ENDPOINT", "value": "5m:/mymetrics,30s:/mymetrics2"}``

Available scrape intervals: 15s, 30s, 1m, 5m.

Default metric path is /metrics. Default interval is 1m.

The following Prometheus configuration should be used to support all available intervals:

```YAML
  - job_name: 'ecs-15s'
    scrape_interval: 15s
    file_sd_configs:
      - files:
          - /opt/prometheus-ecs/15s-tasks.json
    relabel_configs:
      - source_labels: [metrics_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)

  - job_name: 'ecs-30s'
    scrape_interval: 30s
    file_sd_configs:
      - files:
          - /opt/prometheus-ecs/30s-tasks.json
    relabel_configs:
      - source_labels: [metrics_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)

  - job_name: 'ecs-1m'
    scrape_interval: 1m
    file_sd_configs:
      - files:
          - /opt/prometheus-ecs/1m-tasks.json
    relabel_configs:
      - source_labels: [metrics_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)

  - job_name: 'ecs-5m'
    scrape_interval: 5m
    file_sd_configs:
      - files:
          - /opt/prometheus-ecs/5m-tasks.json
    relabel_configs:
      - source_labels: [metrics_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
```

To add tags to the discovered services, set the PROMETHEUS_TAGS ENV variable:

``{"name": "PROMETHEUS_TAGS", "value": ",team=foo,stage=prod,"}``


## EC2 IAM Policy

The following IAM Policy should be added when running discoverecs.py in EC2:

```JSON
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": ["ecs:Describe*", "ecs:List*"],
      "Effect": "Allow",
      "Resource": "*"
    }
```

You will also need EC2 Read Only Access. If you use Terraform:

```hcl
# Prometheus EC2 service discovery
resource "aws_iam_role_policy_attachment" "prometheus-server-role-ec2-read-only" {
  role = "${aws_iam_role.prometheus-server-role.name}"
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"
}
```

### Cross-Account service discovery

To discover services in other AWS accounts, follow the below steps:

- Create the above IAM policy in the target accounts, too
- Create an IAM role in the target accounts with the policy attached and a trust relationship with the Prometheus account so that the discovery service is trusted to assume the role. Trust Policy example:

  ```JSON
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam::111111111111:root"
        },
        "Action": "sts:AssumeRole",
        "Condition": {}
      }
    ]
  }
  ```

- In the account with Prometheus running, add `"sts:AssumeRole"` to the list of allowed actions in the IAM policy
- Provide the Role ARN or multiple Role ARNs to the discovery service with `--role`:

  ```
  python discoverecs.py --directory /opt/prometheus-ecs --role \
    arn:aws:iam::222222222222:role/CrossAccountSdExampleRole \
    arn:aws:iam::333333333333:role/CrossAccountSdExampleRole
  ```


## Special cases
For skipping labels, set PROMETHEUS_NOLABELS to "true".
This is useful when you use "blackbox" exporters or Pushgateway in a task
and metrics are exposed at a service level. This way, no EC2/ECS labels
will be exposed and the instance label will always point to the job name.

## Networking

All network modes are supported (bridge, host and awsvpc).

If PROMETHEUS_PORT and PROMETHEUS_CONTAINER_PORT are not set, the script will pick the first port from the container
definition (in awsvpc and host network mode) or the container host network bindings
in bridge mode. On Fargate, if PROMETHEUS_PORT is not set, it will default to port 80.

If PROMETHEUS_CONTAINER_PORT is set, it will look at the container host network bindings, and find the entry with a matching containerPort. It will then use the hostPort found there as target port.
This is useful when the container port is known, but the hostPort is randomly picked by ECS (by setting hostPort to 0 in the task definition).

If your container uses multiple ports, it's recommended to specify PROMETHEUS_PORT (awsvpc, host) or PROMETHEUS_CONTAINER_PORT (bridge).
