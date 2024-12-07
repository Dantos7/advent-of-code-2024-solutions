"""Init file for aoc package."""

from enum import Enum
from pathlib import Path


class InstanceType(str, Enum):
    """Instance type enum."""

    EXAMPLES = "examples"
    INPUTS = "inputs"


def read_day_instance_lines(instance: InstanceType, day: str) -> list[str]:
    """Read the day instance file and returns its (stripped) lines."""
    with Path(f"data/{instance.value}/{day}.txt").open() as f:
        lines = [line.strip() for line in f]

    return lines


def read_day_instance_matrix(instance: InstanceType, day: str) -> list[str]:
    """Read the day instance file and returns the char matrix in it."""
    lines = read_day_instance_lines(instance, day)

    return lines
