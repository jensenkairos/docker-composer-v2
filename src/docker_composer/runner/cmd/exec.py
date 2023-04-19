# DO NOT EDIT: Autogenerated by /Users/jensen/kairos/docker-composer/src/docker_composer/_utils/generate_class.py
# for Docker Compose version v2.17.2

from typing import List, Optional

import attr

from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeExec(DockerBaseRunner):
    """

    Usage:  docker compose exec [OPTIONS] SERVICE COMMAND [ARGS...]

    Execute a command in a running container.

    """

    detach: Optional[bool] = None
    """Detached mode: Run command in the
       background."""
    env: Optional[str] = None
    """Set environment variables
       --index int                    index of the container if there are
       multiple instances of a service
       [default: 1]. (default 1)"""
    no_TTY: Optional[str] = None
    """Disable pseudo-TTY allocation. By
       default docker compose exec
       allocates a TTY. (default true)
       --privileged                   Give extended privileges to the process."""
    user: Optional[str] = None
    """Run the command as this user."""
    workdir: Optional[str] = None
    """Path to workdir directory for this
       command."""
    _cmd: str = "exec"
    _options: List[str] = [
        "detach",
    ]
