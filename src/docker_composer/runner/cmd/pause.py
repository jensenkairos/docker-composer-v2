# DO NOT EDIT: Autogenerated by /Users/jensen/kairos/docker-composer/src/docker_composer/_utils/generate_class.py
# for Docker Compose version v2.17.2

from typing import List, Optional

import attr

from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposePause(DockerBaseRunner):
    """

    Usage:  docker compose pause [SERVICE...]

    Pause services

    """

    _cmd: str = "pause"
    _options: List[str] = []