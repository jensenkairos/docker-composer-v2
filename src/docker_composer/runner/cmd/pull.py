# DO NOT EDIT: Autogenerated by /Users/jensen/kairos/docker-composer/src/docker_composer/_utils/generate_class.py
# for Docker Compose version v2.17.2

from typing import List, Optional

import attr

from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposePull(DockerBaseRunner):
    """

    Usage:  docker compose pull [OPTIONS] [SERVICE...]

    Pull service images

    """

    ignore_buildable: Optional[bool] = None
    """Ignore images that can be built.
       --ignore-pull-failures   Pull what it can and ignores images with
       pull failures.
       --include-deps           Also pull services declared as dependencies."""
    quiet: Optional[bool] = None
    """Pull without printing progress information."""
    _cmd: str = "pull"
    _options: List[str] = [
        "ignore_buildable",
        "quiet",
    ]
