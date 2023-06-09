# DO NOT EDIT: Autogenerated by /Users/jensen/kairos/docker-composer-v2/src/docker_composer_v2/_utils/generate_class.py
# for Docker Compose version v2.17.2

from typing import List, Optional

import attr

from docker_composer_v2.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeRestart(DockerBaseRunner):
    """

    Usage:  docker compose restart [OPTIONS] [SERVICE...]

    Restart service containers

    """

    no_deps: Optional[bool] = None
    """Don't restart dependent services."""
    timeout: Optional[int] = None
    """Specify a shutdown timeout in seconds (default 10)"""
    _cmd: str = "restart"
    _options: List[str] = [
        "no_deps",
    ]
