# DO NOT EDIT: Autogenerated by /Users/jensen/kairos/docker-composer/src/docker_composer/_utils/generate_class.py
# for Docker Compose version v2.17.2

from typing import List, Optional

import attr

from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeRm(DockerBaseRunner):
    """

    Usage:  docker compose rm [OPTIONS] [SERVICE...]

    Removes stopped service containers

    By default, anonymous volumes attached to containers will not be removed. You
    can override this with -v. To list all volumes, use "docker volume ls".

    Any data which is not in a volume will be lost.

    """

    force: Optional[bool] = None
    """Don't ask to confirm removal"""
    stop: Optional[bool] = None
    """Stop the containers, if required, before removing"""
    volumes: Optional[bool] = None
    """Remove any anonymous volumes attached to containers"""
    _cmd: str = "rm"
    _options: List[str] = [
        "force",
        "stop",
        "volumes",
    ]
