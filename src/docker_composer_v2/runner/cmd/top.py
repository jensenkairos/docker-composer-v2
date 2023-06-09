# DO NOT EDIT: Autogenerated by /Users/jensen/kairos/docker-composer-v2/src/docker_composer_v2/_utils/generate_class.py
# for Docker Compose version v2.17.2

from typing import List, Optional

import attr

from docker_composer_v2.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeTop(DockerBaseRunner):
    """

    Usage:  docker compose top [SERVICES...]

    Display the running processes

    """

    _cmd: str = "top"
    _options: List[str] = []
