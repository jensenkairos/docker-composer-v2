# DO NOT EDIT: Autogenerated by /Users/jensen/kairos/docker-composer/src/docker_composer/_utils/generate_class.py
# for Docker Compose version v2.17.2

from typing import List, Optional

import attr

from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeLogs(DockerBaseRunner):
    """

    Usage:  docker compose logs [OPTIONS] [SERVICE...]

    View output from containers

    """

    follow: Optional[bool] = None
    """Follow log output.
       --no-color        Produce monochrome output.
       --no-log-prefix   Don't print prefix in logs.
       --since string    Show logs since timestamp (e.g.
       2013-01-02T13:23:37Z) or relative (e.g. 42m for
       42 minutes)"""
    tail: Optional[str] = None
    """Number of lines to show from the end of the logs
       for each container. (default "all")"""
    timestamps: Optional[bool] = None
    """Show timestamps.
       --until string    Show logs before a timestamp (e.g.
       2013-01-02T13:23:37Z) or relative (e.g. 42m for
       42 minutes)"""
    _cmd: str = "logs"
    _options: List[str] = [
        "follow",
        "timestamps",
    ]
