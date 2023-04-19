# DO NOT EDIT: Autogenerated by /Users/jensen/kairos/docker-composer/src/docker_composer/_utils/generate_class.py
# for Docker Compose version v2.17.2

from typing import List, Optional

import attr

from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeDown(DockerBaseRunner):
    """

    Usage:  docker compose down [OPTIONS]

    Stop and remove containers, networks

    """

    remove_orphans: Optional[bool] = None
    """Remove containers for services not defined in
       the Compose file.
       --rmi string        Remove images used by services. "local" remove
       only images that don't have a custom tag
       ("local"|"all")"""
    timeout: Optional[int] = None
    """Specify a shutdown timeout in seconds (default 10)"""
    volumes: Optional[str] = None
    """Remove named volumes declared in the volumes
       section of the Compose file and anonymous
       volumes attached to containers."""
    _cmd: str = "down"
    _options: List[str] = [
        "remove_orphans",
    ]
