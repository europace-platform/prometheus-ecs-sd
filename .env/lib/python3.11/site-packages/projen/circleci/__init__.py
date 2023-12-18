import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

from .. import (
    Component as _Component_2b0ad27f,
    Project as _Project_57d89203,
    YamlFile as _YamlFile_909731b0,
)


@jsii.data_type(
    jsii_type="projen.circleci.CircleCiProps",
    jsii_struct_bases=[],
    name_mapping={
        "jobs": "jobs",
        "orbs": "orbs",
        "setup": "setup",
        "version": "version",
        "workflows": "workflows",
    },
)
class CircleCiProps:
    def __init__(
        self,
        *,
        jobs: typing.Optional[typing.Sequence["Job"]] = None,
        orbs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        setup: typing.Optional[builtins.bool] = None,
        version: typing.Optional[jsii.Number] = None,
        workflows: typing.Optional[typing.Sequence["Workflow"]] = None,
    ) -> None:
        '''(experimental) Options for class {@link Circleci}.

        :param jobs: (experimental) List of Jobs to create unique steps per pipeline, e.g. ``json jobs: [{ identifier: "compile", docker: { image: "golang:alpine" } steps: ["checkout", run: {command: "go build ."}] }] ``.
        :param orbs: (experimental) Contains a map of CirclCi Orbs ``json orbs: { node: "circleci/node@5.0.1" slack: "circleci/slack@4.8.3" } ``.
        :param setup: (experimental) The setup field enables you to conditionally trigger configurations from outside the primary .circleci parent directory, update pipeline parameters, or generate customized configurations.
        :param version: (experimental) pipeline version. Default: 2.1
        :param workflows: (experimental) List of Workflows of pipeline, e.g. ``json workflows: { { identifier: "build", jobs: [{ identifier: "node/install", context: ["npm"], }] } } ``.

        :see: https://circleci.com/docs/2.0/configuration-reference/
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if jobs is not None:
            self._values["jobs"] = jobs
        if orbs is not None:
            self._values["orbs"] = orbs
        if setup is not None:
            self._values["setup"] = setup
        if version is not None:
            self._values["version"] = version
        if workflows is not None:
            self._values["workflows"] = workflows

    @builtins.property
    def jobs(self) -> typing.Optional[typing.List["Job"]]:
        '''(experimental) List of Jobs to create unique steps per pipeline, e.g. ``json jobs: [{   identifier: "compile",   docker: { image: "golang:alpine" }   steps: ["checkout", run: {command: "go build ."}] }] ``.

        :see: https://circleci.com/docs/2.0/configuration-reference/#jobs
        :stability: experimental
        '''
        result = self._values.get("jobs")
        return typing.cast(typing.Optional[typing.List["Job"]], result)

    @builtins.property
    def orbs(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Contains a map of CirclCi Orbs ``json orbs: {   node: "circleci/node@5.0.1"   slack: "circleci/slack@4.8.3" } ``.

        :stability: experimental
        '''
        result = self._values.get("orbs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def setup(self) -> typing.Optional[builtins.bool]:
        '''(experimental) The setup field enables you to conditionally trigger configurations from outside the primary .circleci parent directory, update pipeline parameters, or generate customized configurations.

        :see: https://circleci.com/docs/2.0/configuration-reference/#setup
        :stability: experimental
        '''
        result = self._values.get("setup")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''(experimental) pipeline version.

        :default: 2.1

        :see: https://circleci.com/docs/2.0/configuration-reference/#version
        :stability: experimental
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def workflows(self) -> typing.Optional[typing.List["Workflow"]]:
        '''(experimental) List of Workflows of pipeline, e.g. ``json workflows: {    {      identifier: "build",        jobs: [{           identifier: "node/install",           context: ["npm"],        }]    } } ``.

        :see: https://circleci.com/docs/2.0/configuration-reference/#workflows
        :stability: experimental
        '''
        result = self._values.get("workflows")
        return typing.cast(typing.Optional[typing.List["Workflow"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CircleCiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Circleci(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.circleci.Circleci",
):
    '''(experimental) Circleci Class to manage ``.circleci/config.yml``. Check projen's docs for more information.

    :see: https://circleci.com/docs/2.0/configuration-reference/
    :stability: experimental
    '''

    def __init__(
        self,
        project: _Project_57d89203,
        *,
        jobs: typing.Optional[typing.Sequence["Job"]] = None,
        orbs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        setup: typing.Optional[builtins.bool] = None,
        version: typing.Optional[jsii.Number] = None,
        workflows: typing.Optional[typing.Sequence["Workflow"]] = None,
    ) -> None:
        '''
        :param project: -
        :param jobs: (experimental) List of Jobs to create unique steps per pipeline, e.g. ``json jobs: [{ identifier: "compile", docker: { image: "golang:alpine" } steps: ["checkout", run: {command: "go build ."}] }] ``.
        :param orbs: (experimental) Contains a map of CirclCi Orbs ``json orbs: { node: "circleci/node@5.0.1" slack: "circleci/slack@4.8.3" } ``.
        :param setup: (experimental) The setup field enables you to conditionally trigger configurations from outside the primary .circleci parent directory, update pipeline parameters, or generate customized configurations.
        :param version: (experimental) pipeline version. Default: 2.1
        :param workflows: (experimental) List of Workflows of pipeline, e.g. ``json workflows: { { identifier: "build", jobs: [{ identifier: "node/install", context: ["npm"], }] } } ``.

        :stability: experimental
        '''
        options = CircleCiProps(
            jobs=jobs, orbs=orbs, setup=setup, version=version, workflows=workflows
        )

        jsii.create(self.__class__, self, [project, options])

    @jsii.member(jsii_name="addOrb")
    def add_orb(self, name: builtins.str, orb: builtins.str) -> None:
        '''(experimental) Add a Circleci Orb to pipeline.

        Will throw error if the orb already exists

        :param name: -
        :param orb: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addOrb", [name, orb]))

    @jsii.member(jsii_name="addWorkflow")
    def add_workflow(
        self,
        *,
        identifier: builtins.str,
        jobs: typing.Optional[typing.Sequence["WorkflowJob"]] = None,
        triggers: typing.Optional[typing.Sequence["Triggers"]] = None,
        when: typing.Any = None,
    ) -> None:
        '''(experimental) add new workflow to existing pipeline.

        :param identifier: (experimental) name of dynamic key *.
        :param jobs: 
        :param triggers: 
        :param when: (experimental) when is too dynamic to be casted to interfaces. Check Docu as reference

        :stability: experimental
        '''
        workflow = Workflow(
            identifier=identifier, jobs=jobs, triggers=triggers, when=when
        )

        return typing.cast(None, jsii.invoke(self, "addWorkflow", [workflow]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="file")
    def file(self) -> _YamlFile_909731b0:
        '''(experimental) The yaml file for the Circleci pipeline.

        :stability: experimental
        '''
        return typing.cast(_YamlFile_909731b0, jsii.get(self, "file"))


@jsii.data_type(
    jsii_type="projen.circleci.Docker",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "auth": "auth",
        "aws_auth": "awsAuth",
        "command": "command",
        "entrypoint": "entrypoint",
        "environment": "environment",
        "name": "name",
        "user": "user",
    },
)
class Docker:
    def __init__(
        self,
        *,
        image: builtins.str,
        auth: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        aws_auth: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]] = None,
        name: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Options for docker executor.

        :param image: (experimental) The name of a custom docker image to use.
        :param auth: (experimental) Authentication for registries using standard docker login credentials.
        :param aws_auth: (experimental) Authentication for AWS Elastic Container Registry (ECR).
        :param command: (experimental) The command used as pid 1 (or args for entrypoint) when launching the container.
        :param entrypoint: (experimental) The command used as executable when launching the container.
        :param environment: (experimental) A map of environment variable names and values.
        :param name: (experimental) The name the container is reachable by. By default, container services are accessible through localhost
        :param user: (experimental) Which user to run commands as within the Docker container.

        :see: https://circleci.com/docs/2.0/configuration-reference/#docker
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
        }
        if auth is not None:
            self._values["auth"] = auth
        if aws_auth is not None:
            self._values["aws_auth"] = aws_auth
        if command is not None:
            self._values["command"] = command
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if environment is not None:
            self._values["environment"] = environment
        if name is not None:
            self._values["name"] = name
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def image(self) -> builtins.str:
        '''(experimental) The name of a custom docker image to use.

        :stability: experimental
        '''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Authentication for registries using standard docker login credentials.

        :stability: experimental
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def aws_auth(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Authentication for AWS Elastic Container Registry (ECR).

        :stability: experimental
        '''
        result = self._values.get("aws_auth")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The command used as pid 1 (or args for entrypoint) when launching the container.

        :stability: experimental
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The command used as executable when launching the container.

        :stability: experimental
        '''
        result = self._values.get("entrypoint")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]]:
        '''(experimental) A map of environment variable names and values.

        :stability: experimental
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name the container is reachable by.

        By default, container services are accessible through localhost

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''(experimental) Which user to run commands as within the Docker container.

        :stability: experimental
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Docker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.circleci.Filter",
    jsii_struct_bases=[],
    name_mapping={"branches": "branches", "tags": "tags"},
)
class Filter:
    def __init__(
        self,
        *,
        branches: typing.Optional["FilterConfig"] = None,
        tags: typing.Optional["FilterConfig"] = None,
    ) -> None:
        '''(experimental) The branches key controls whether the current branch should have a schedule trigger created for it, where current branch is the branch containing the config.yml file with the trigger stanza. That is, a push on the main branch will only schedule a workflow for the main branch.

        Branches can have the keys only and ignore which either map to a single string naming a branch.
        You may also use regular expressions to match against branches by enclosing them with /’s, or map to a list of such strings.
        Regular expressions must match the entire string.

        Any branches that match only will run the job.
        Any branches that match ignore will not run the job.
        If neither only nor ignore are specified then all branches will run the job.
        If both only and ignore are specified the only is considered before ignore.

        :param branches: 
        :param tags: 

        :see: https://circleci.com/docs/2.0/configuration-reference/#filters
        :stability: experimental
        '''
        if isinstance(branches, dict):
            branches = FilterConfig(**branches)
        if isinstance(tags, dict):
            tags = FilterConfig(**tags)
        self._values: typing.Dict[str, typing.Any] = {}
        if branches is not None:
            self._values["branches"] = branches
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def branches(self) -> typing.Optional["FilterConfig"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("branches")
        return typing.cast(typing.Optional["FilterConfig"], result)

    @builtins.property
    def tags(self) -> typing.Optional["FilterConfig"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["FilterConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Filter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.circleci.FilterConfig",
    jsii_struct_bases=[],
    name_mapping={"ignore": "ignore", "only": "only"},
)
class FilterConfig:
    def __init__(
        self,
        *,
        ignore: typing.Optional[typing.Sequence[builtins.str]] = None,
        only: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) set an inclusive or exclusive filter.

        :param ignore: (experimental) Either a single branch specifier, or a list of branch specifiers.
        :param only: (experimental) Either a single branch specifier, or a list of branch specifiers.

        :see: https://circleci.com/docs/2.0/configuration-reference/#filters
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ignore is not None:
            self._values["ignore"] = ignore
        if only is not None:
            self._values["only"] = only

    @builtins.property
    def ignore(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Either a single branch specifier, or a list of branch specifiers.

        :stability: experimental
        '''
        result = self._values.get("ignore")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def only(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Either a single branch specifier, or a list of branch specifiers.

        :stability: experimental
        '''
        result = self._values.get("only")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FilterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.circleci.Job",
    jsii_struct_bases=[],
    name_mapping={
        "identifier": "identifier",
        "docker": "docker",
        "environment": "environment",
        "machine": "machine",
        "macos": "macos",
        "parallelism": "parallelism",
        "parameters": "parameters",
        "resource_class": "resourceClass",
        "shell": "shell",
        "steps": "steps",
        "working_directory": "workingDirectory",
    },
)
class Job:
    def __init__(
        self,
        *,
        identifier: builtins.str,
        docker: typing.Optional[typing.Sequence[Docker]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]] = None,
        machine: typing.Optional["Machine"] = None,
        macos: typing.Optional["Macos"] = None,
        parallelism: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        resource_class: typing.Optional[builtins.str] = None,
        shell: typing.Optional[builtins.str] = None,
        steps: typing.Optional[typing.Sequence[typing.Any]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) A Workflow is comprised of one or more uniquely named jobs.

        Jobs are specified in the jobs map,
        see Sample 2.0 config.yml for two examples of a job map.
        The name of the job is the key in the map, and the value is a map describing the job.
        Each job consists of the job’s name as a key and a map as a value. A name should be case insensitive unique within a current jobs list.

        :param identifier: (experimental) name of dynamic key *.
        :param docker: 
        :param environment: (experimental) A map of environment variable names and values.
        :param machine: 
        :param macos: 
        :param parallelism: (experimental) Number of parallel instances of this job to run (default: 1).
        :param parameters: (experimental) Parameters for making a job explicitly configurable in a workflow.
        :param resource_class: (experimental) {@link ResourceClass}.
        :param shell: (experimental) Shell to use for execution command in all steps. Can be overridden by shell in each step
        :param steps: (experimental) no type support here, for syntax {@see https://circleci.com/docs/2.0/configuration-reference/#steps}.
        :param working_directory: (experimental) In which directory to run the steps. Will be interpreted as an absolute path. Default: ``~/project``

        :see: https://circleci.com/docs/2.0/configuration-reference/#job_name
        :stability: experimental
        '''
        if isinstance(machine, dict):
            machine = Machine(**machine)
        if isinstance(macos, dict):
            macos = Macos(**macos)
        self._values: typing.Dict[str, typing.Any] = {
            "identifier": identifier,
        }
        if docker is not None:
            self._values["docker"] = docker
        if environment is not None:
            self._values["environment"] = environment
        if machine is not None:
            self._values["machine"] = machine
        if macos is not None:
            self._values["macos"] = macos
        if parallelism is not None:
            self._values["parallelism"] = parallelism
        if parameters is not None:
            self._values["parameters"] = parameters
        if resource_class is not None:
            self._values["resource_class"] = resource_class
        if shell is not None:
            self._values["shell"] = shell
        if steps is not None:
            self._values["steps"] = steps
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def identifier(self) -> builtins.str:
        '''(experimental) name of dynamic key *.

        :stability: experimental
        '''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def docker(self) -> typing.Optional[typing.List[Docker]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("docker")
        return typing.cast(typing.Optional[typing.List[Docker]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]]:
        '''(experimental) A map of environment variable names and values.

        :stability: experimental
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]], result)

    @builtins.property
    def machine(self) -> typing.Optional["Machine"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("machine")
        return typing.cast(typing.Optional["Machine"], result)

    @builtins.property
    def macos(self) -> typing.Optional["Macos"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("macos")
        return typing.cast(typing.Optional["Macos"], result)

    @builtins.property
    def parallelism(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Number of parallel instances of this job to run (default: 1).

        :stability: experimental
        '''
        result = self._values.get("parallelism")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Parameters for making a job explicitly configurable in a workflow.

        :stability: experimental
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def resource_class(self) -> typing.Optional[builtins.str]:
        '''(experimental) {@link ResourceClass}.

        :stability: experimental
        '''
        result = self._values.get("resource_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shell(self) -> typing.Optional[builtins.str]:
        '''(experimental) Shell to use for execution command in all steps.

        Can be overridden by shell in each step

        :stability: experimental
        '''
        result = self._values.get("shell")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def steps(self) -> typing.Optional[typing.List[typing.Any]]:
        '''(experimental) no type support here, for syntax {@see https://circleci.com/docs/2.0/configuration-reference/#steps}.

        :stability: experimental
        '''
        result = self._values.get("steps")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''(experimental) In which directory to run the steps.

        Will be interpreted as an absolute path. Default: ``~/project``

        :stability: experimental
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Job(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.circleci.JobType")
class JobType(enum.Enum):
    '''(experimental) A job may have a type of approval indicating it must be manually approved before downstream jobs may proceed.

    :see: https://circleci.com/docs/2.0/configuration-reference/#type
    :stability: experimental
    '''

    APPROVAL = "APPROVAL"
    '''
    :stability: experimental
    '''


@jsii.enum(jsii_type="projen.circleci.JobWhen")
class JobWhen(enum.Enum):
    '''(experimental) Specify when to enable or disable the step.

    :see: https://circleci.com/docs/2.0/configuration-reference/#steps
    :stability: experimental
    '''

    ALWAYS = "ALWAYS"
    '''
    :stability: experimental
    '''
    ON_SUCCESS = "ON_SUCCESS"
    '''
    :stability: experimental
    '''
    ON_FAIL = "ON_FAIL"
    '''
    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="projen.circleci.Machine",
    jsii_struct_bases=[],
    name_mapping={"image": "image", "docker_layer_caching": "dockerLayerCaching"},
)
class Machine:
    def __init__(
        self,
        *,
        image: builtins.str,
        docker_layer_caching: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image: (experimental) The VM image to use.
        :param docker_layer_caching: (experimental) enable docker layer caching.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
        }
        if docker_layer_caching is not None:
            self._values["docker_layer_caching"] = docker_layer_caching

    @builtins.property
    def image(self) -> builtins.str:
        '''(experimental) The VM image to use.

        :see: https://circleci.com/docs/2.0/configuration-reference/#available-machine-images
        :stability: experimental
        '''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def docker_layer_caching(self) -> typing.Optional[builtins.str]:
        '''(experimental) enable docker layer caching.

        :see: https://circleci.com/docs/2.0/configuration-reference/#available-machine-images
        :stability: experimental
        '''
        result = self._values.get("docker_layer_caching")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Machine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.circleci.Macos",
    jsii_struct_bases=[],
    name_mapping={"xcode": "xcode"},
)
class Macos:
    def __init__(self, *, xcode: builtins.str) -> None:
        '''(experimental) CircleCI supports running jobs on macOS, to allow you to build, test, and deploy apps for macOS, iOS, tvOS and watchOS.

        To run a job in a macOS virtual machine,
        you must add the macos key to the top-level configuration for the job and specify
        the version of Xcode you would like to use.

        :param xcode: (experimental) The version of Xcode that is installed on the virtual machine.

        :see: https://circleci.com/docs/2.0/configuration-reference/#macos
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "xcode": xcode,
        }

    @builtins.property
    def xcode(self) -> builtins.str:
        '''(experimental) The version of Xcode that is installed on the virtual machine.

        :stability: experimental
        '''
        result = self._values.get("xcode")
        assert result is not None, "Required property 'xcode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macos(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.circleci.Matrix",
    jsii_struct_bases=[],
    name_mapping={"alias": "alias", "parameters": "parameters"},
)
class Matrix:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.Sequence[builtins.str], typing.Sequence[jsii.Number]]]] = None,
    ) -> None:
        '''(experimental) The matrix stanza allows you to run a parameterized job multiple times with different arguments.

        :param alias: (experimental) An alias for the matrix, usable from another job’s requires stanza. Defaults to the name of the job being executed
        :param parameters: (experimental) A map of parameter names to every value the job should be called with.

        :see: https://circleci.com/docs/2.0/configuration-reference/#matrix-requires-version-21
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''(experimental) An alias for the matrix, usable from another job’s requires stanza.

        Defaults to the name of the job being executed

        :stability: experimental
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.List[builtins.str], typing.List[jsii.Number]]]]:
        '''(experimental) A map of parameter names to every value the job should be called with.

        :stability: experimental
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[typing.List[builtins.str], typing.List[jsii.Number]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Matrix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.circleci.ResourceClass")
class ResourceClass(enum.Enum):
    '''(experimental) The resource_class feature allows configuring CPU and RAM resources for each job.

    Different resource classes are available for different executors, as described in the tables below.

    :see: https://circleci.com/docs/2.0/configuration-reference/#resourceclass
    :stability: experimental
    '''

    SMALL = "SMALL"
    '''
    :stability: experimental
    '''
    MEDIUM = "MEDIUM"
    '''
    :stability: experimental
    '''
    MEDIUM_PLUS = "MEDIUM_PLUS"
    '''
    :stability: experimental
    '''
    LARGE_X = "LARGE_X"
    '''
    :stability: experimental
    '''
    LARGE_2X = "LARGE_2X"
    '''
    :stability: experimental
    '''
    LARGE_2X_PLUS = "LARGE_2X_PLUS"
    '''
    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="projen.circleci.Run",
    jsii_struct_bases=[],
    name_mapping={
        "command": "command",
        "background": "background",
        "environment": "environment",
        "name": "name",
        "no_output_timeout": "noOutputTimeout",
        "shell": "shell",
        "when": "when",
        "working_directory": "workingDirectory",
    },
)
class Run:
    def __init__(
        self,
        *,
        command: builtins.str,
        background: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        no_output_timeout: typing.Optional[builtins.str] = None,
        shell: typing.Optional[builtins.str] = None,
        when: typing.Optional[builtins.str] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Used for invoking all command-line programs, taking either a map of configuration values, or, when called in its short-form, a string that will be used as both the command and name.

        Run commands are executed using non-login shells by default,
        so you must explicitly source any dotfiles as part of the command.

        Not used because type incompatible types in steps array

        :param command: (experimental) Command to run via the shell.
        :param background: (experimental) Whether this step should run in the background (default: false).
        :param environment: (experimental) Additional environmental variables, locally scoped to command.
        :param name: (experimental) Title of the step to be shown in the CircleCI UI (default: full command).
        :param no_output_timeout: (experimental) Elapsed time the command can run without output such as “20m”, “1.25h”, “5s”. The default is 10 minutes.
        :param shell: (experimental) Shell to use for execution command.
        :param when: (experimental) Specify when to enable or disable the step.
        :param working_directory: (experimental) In which directory to run this step. Will be interpreted relative to the working_directory of the job). (default: .)

        :see: https://circleci.com/docs/2.0/configuration-reference/#run
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "command": command,
        }
        if background is not None:
            self._values["background"] = background
        if environment is not None:
            self._values["environment"] = environment
        if name is not None:
            self._values["name"] = name
        if no_output_timeout is not None:
            self._values["no_output_timeout"] = no_output_timeout
        if shell is not None:
            self._values["shell"] = shell
        if when is not None:
            self._values["when"] = when
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def command(self) -> builtins.str:
        '''(experimental) Command to run via the shell.

        :stability: experimental
        '''
        result = self._values.get("command")
        assert result is not None, "Required property 'command' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def background(self) -> typing.Optional[builtins.str]:
        '''(experimental) Whether this step should run in the background (default: false).

        :stability: experimental
        '''
        result = self._values.get("background")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''(experimental) Additional environmental variables, locally scoped to command.

        :stability: experimental
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Title of the step to be shown in the CircleCI UI (default: full command).

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_output_timeout(self) -> typing.Optional[builtins.str]:
        '''(experimental) Elapsed time the command can run without output such as “20m”, “1.25h”, “5s”. The default is 10 minutes.

        :stability: experimental
        '''
        result = self._values.get("no_output_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shell(self) -> typing.Optional[builtins.str]:
        '''(experimental) Shell to use for execution command.

        :stability: experimental
        '''
        result = self._values.get("shell")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def when(self) -> typing.Optional[builtins.str]:
        '''(experimental) Specify when to enable or disable the step.

        :stability: experimental
        '''
        result = self._values.get("when")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''(experimental) In which directory to run this step.

        Will be interpreted relative to the working_directory of the job). (default: .)

        :stability: experimental
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Run(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.circleci.Schedule",
    jsii_struct_bases=[],
    name_mapping={"filters": "filters", "cron": "cron"},
)
class Schedule:
    def __init__(
        self,
        *,
        filters: Filter,
        cron: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) A workflow may have a schedule indicating it runs at a certain time.

        :param filters: 
        :param cron: (experimental) The cron key is defined using POSIX crontab syntax.

        :see: https://circleci.com/docs/2.0/configuration-reference/#schedule
        :stability: experimental
        '''
        if isinstance(filters, dict):
            filters = Filter(**filters)
        self._values: typing.Dict[str, typing.Any] = {
            "filters": filters,
        }
        if cron is not None:
            self._values["cron"] = cron

    @builtins.property
    def filters(self) -> Filter:
        '''
        :stability: experimental
        '''
        result = self._values.get("filters")
        assert result is not None, "Required property 'filters' is missing"
        return typing.cast(Filter, result)

    @builtins.property
    def cron(self) -> typing.Optional[builtins.str]:
        '''(experimental) The cron key is defined using POSIX crontab syntax.

        :stability: experimental
        '''
        result = self._values.get("cron")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Schedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.circleci.StepRun",
    jsii_struct_bases=[],
    name_mapping={"run": "run"},
)
class StepRun:
    def __init__(self, *, run: typing.Optional[Run] = None) -> None:
        '''(experimental) Execution steps for Job.

        :param run: 

        :see: https://circleci.com/docs/2.0/configuration-reference/#steps
        :stability: experimental
        '''
        if isinstance(run, dict):
            run = Run(**run)
        self._values: typing.Dict[str, typing.Any] = {}
        if run is not None:
            self._values["run"] = run

    @builtins.property
    def run(self) -> typing.Optional[Run]:
        '''
        :stability: experimental
        '''
        result = self._values.get("run")
        return typing.cast(typing.Optional[Run], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StepRun(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.circleci.Triggers",
    jsii_struct_bases=[],
    name_mapping={"schedule": "schedule"},
)
class Triggers:
    def __init__(self, *, schedule: typing.Optional[Schedule] = None) -> None:
        '''(experimental) Specifies which triggers will cause this workflow to be executed.

        Default behavior is to trigger the workflow when pushing to a branch.

        :param schedule: 

        :see: https://circleci.com/docs/2.0/configuration-reference/#triggers
        :stability: experimental
        '''
        if isinstance(schedule, dict):
            schedule = Schedule(**schedule)
        self._values: typing.Dict[str, typing.Any] = {}
        if schedule is not None:
            self._values["schedule"] = schedule

    @builtins.property
    def schedule(self) -> typing.Optional[Schedule]:
        '''
        :stability: experimental
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[Schedule], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Triggers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.circleci.Workflow",
    jsii_struct_bases=[],
    name_mapping={
        "identifier": "identifier",
        "jobs": "jobs",
        "triggers": "triggers",
        "when": "when",
    },
)
class Workflow:
    def __init__(
        self,
        *,
        identifier: builtins.str,
        jobs: typing.Optional[typing.Sequence["WorkflowJob"]] = None,
        triggers: typing.Optional[typing.Sequence[Triggers]] = None,
        when: typing.Any = None,
    ) -> None:
        '''(experimental) Used for orchestrating all jobs.

        Each workflow consists of the workflow name as a key and a map as a value.
        A name should be unique within the current config.yml.
        The top-level keys for the Workflows configuration are version and jobs.

        :param identifier: (experimental) name of dynamic key *.
        :param jobs: 
        :param triggers: 
        :param when: (experimental) when is too dynamic to be casted to interfaces. Check Docu as reference

        :see: https://circleci.com/docs/2.0/configuration-reference/#workflows
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "identifier": identifier,
        }
        if jobs is not None:
            self._values["jobs"] = jobs
        if triggers is not None:
            self._values["triggers"] = triggers
        if when is not None:
            self._values["when"] = when

    @builtins.property
    def identifier(self) -> builtins.str:
        '''(experimental) name of dynamic key *.

        :stability: experimental
        '''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def jobs(self) -> typing.Optional[typing.List["WorkflowJob"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("jobs")
        return typing.cast(typing.Optional[typing.List["WorkflowJob"]], result)

    @builtins.property
    def triggers(self) -> typing.Optional[typing.List[Triggers]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.List[Triggers]], result)

    @builtins.property
    def when(self) -> typing.Any:
        '''(experimental) when is too dynamic to be casted to interfaces.

        Check Docu as reference

        :see: https://circleci.com/docs/2.0/configuration-reference/#logic-statement-examples
        :stability: experimental
        '''
        result = self._values.get("when")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Workflow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.circleci.WorkflowJob",
    jsii_struct_bases=[],
    name_mapping={
        "identifier": "identifier",
        "context": "context",
        "filters": "filters",
        "matrix": "matrix",
        "name": "name",
        "orb_parameters": "orbParameters",
        "parameters": "parameters",
        "requires": "requires",
        "type": "type",
    },
)
class WorkflowJob:
    def __init__(
        self,
        *,
        identifier: builtins.str,
        context: typing.Optional[typing.Sequence[builtins.str]] = None,
        filters: typing.Optional[Filter] = None,
        matrix: typing.Optional[Matrix] = None,
        name: typing.Optional[builtins.str] = None,
        orb_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]] = None,
        requires: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[JobType] = None,
    ) -> None:
        '''(experimental) A Job is part of Workflow.

        A Job can be created with {@link Job} or it can be provided by the orb

        :param identifier: (experimental) name of dynamic key *.
        :param context: (experimental) The name of the context(s). The initial default name is org-global. Each context name must be unique.
        :param filters: (experimental) Job Filters can have the key branches or tags.
        :param matrix: 
        :param name: (experimental) A replacement for the job name. Useful when calling a job multiple times
        :param orb_parameters: (experimental) Parameters passed to job when referencing a job from orb.
        :param parameters: (experimental) Parameters for making a job explicitly configurable in a workflow.
        :param requires: (experimental) A list of jobs that must succeed for the job to start.
        :param type: (experimental) A job may have a type of approval indicating it must be manually approved before downstream jobs may proceed.

        :see: https://circleci.com/docs/2.0/configuration-reference/#jobs-in-workflow
        :stability: experimental
        '''
        if isinstance(filters, dict):
            filters = Filter(**filters)
        if isinstance(matrix, dict):
            matrix = Matrix(**matrix)
        self._values: typing.Dict[str, typing.Any] = {
            "identifier": identifier,
        }
        if context is not None:
            self._values["context"] = context
        if filters is not None:
            self._values["filters"] = filters
        if matrix is not None:
            self._values["matrix"] = matrix
        if name is not None:
            self._values["name"] = name
        if orb_parameters is not None:
            self._values["orb_parameters"] = orb_parameters
        if parameters is not None:
            self._values["parameters"] = parameters
        if requires is not None:
            self._values["requires"] = requires
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def identifier(self) -> builtins.str:
        '''(experimental) name of dynamic key *.

        :stability: experimental
        '''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def context(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The name of the context(s).

        The initial default name is org-global. Each context name must be unique.

        :stability: experimental
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def filters(self) -> typing.Optional[Filter]:
        '''(experimental) Job Filters can have the key branches or tags.

        :stability: experimental
        '''
        result = self._values.get("filters")
        return typing.cast(typing.Optional[Filter], result)

    @builtins.property
    def matrix(self) -> typing.Optional[Matrix]:
        '''
        :stability: experimental
        '''
        result = self._values.get("matrix")
        return typing.cast(typing.Optional[Matrix], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A replacement for the job name.

        Useful when calling a job multiple times

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def orb_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]]:
        '''(experimental) Parameters passed to job when referencing a job from orb.

        :stability: experimental
        '''
        result = self._values.get("orb_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]]:
        '''(experimental) Parameters for making a job explicitly configurable in a workflow.

        :stability: experimental
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, builtins.bool]]], result)

    @builtins.property
    def requires(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) A list of jobs that must succeed for the job to start.

        :stability: experimental
        '''
        result = self._values.get("requires")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[JobType]:
        '''(experimental) A job may have a type of approval indicating it must be manually approved before downstream jobs may proceed.

        :stability: experimental
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[JobType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CircleCiProps",
    "Circleci",
    "Docker",
    "Filter",
    "FilterConfig",
    "Job",
    "JobType",
    "JobWhen",
    "Machine",
    "Macos",
    "Matrix",
    "ResourceClass",
    "Run",
    "Schedule",
    "StepRun",
    "Triggers",
    "Workflow",
    "WorkflowJob",
]

publication.publish()
