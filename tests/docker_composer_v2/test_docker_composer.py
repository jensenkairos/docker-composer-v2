import pytest

import os

from docker_composer_v2 import DockerCompose


@pytest.mark.parametrize(
    "root_args, expected",
    [
        (dict(), []),
        (dict(file="file.yml"), ["--file", "file.yml"]),
        (
            dict(file="docker-compose.yml"),
            [
                "--file",
                "docker-compose.yml",
            ],
        ),
    ],
)
def test_root__call_cmd(root_args, expected):
    res = DockerCompose(**root_args)._call_cmd(["bar"])
    assert res == ["docker", "--log-level", "info", "compose"] + expected + ["bar"]


@pytest.mark.parametrize(
    "cmd_args, expected_cmd",
    [
        (dict(), []),
        (dict(build_arg="Foo"), ["--build-arg", "Foo"]),
    ],
)
def test_build__call_cmd(cmd_args, expected_cmd):
    os.environ["DOCKER_COMPOSE_LOG_LEVEL"] = "debug"
    res = DockerCompose().build(**cmd_args)._call_cmd(["bar"])
    assert (
        res
        == [
            "docker",
            "--log-level",
            "debug",
            "compose",
            "build",
        ]
        + expected_cmd
        + ["bar"]
    )
    os.environ["DOCKER_COMPOSE_LOG_LEVEL"] = "fatal"
    res = DockerCompose().build(**cmd_args)._call_cmd(["bar"])
    assert (
        res
        == [
            "docker",
            "--log-level",
            "fatal",
            "compose",
            "build",
        ]
        + expected_cmd
        + ["bar"]
    )
