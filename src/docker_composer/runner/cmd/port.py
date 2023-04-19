# DO NOT EDIT: Autogenerated by /Users/jensen/kairos/docker-composer/src/docker_composer/_utils/generate_class.py
# for Docker Compose version v2.17.2

from typing import List, Optional

import attr

from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposePort(DockerBaseRunner):
    """

    Usage:  docker compose port [OPTIONS] SERVICE PRIVATE_PORT

    Print the public port for a port binding.

    """

    index: Optional[int] = None
    """index of the container if service has multiple
       replicas (default 1)
       --protocol string   tcp or udp (default "tcp")"""
    _cmd: str = "port"
    _options: List[str] = []