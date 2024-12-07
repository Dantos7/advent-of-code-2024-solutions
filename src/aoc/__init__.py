"""Init file for aoc package."""

from enum import Enum
from pathlib import Path

import numpy as np


class InstanceType(str, Enum):
    """Instance type enum."""

    EXAMPLES = "examples"
    INPUTS = "inputs"


def read_day_instance_lines(instance: InstanceType, day: str) -> list[str]:
    """Read the day instance file and returns its (stripped) lines."""
    with Path(f"data/{instance.value}/{day}.txt").open() as f:
        lines = [line.strip() for line in f]

    return lines


def read_day_instance_matrix(instance: InstanceType, day: str) -> list[list[str]]:
    """Read the day instance file and returns the char matrix in it."""
    lines = read_day_instance_lines(instance, day)
    matrix = [list(line) for line in lines]

    return matrix


def convert_matrix_to_numpy(matrix: list[list[str]], mapping: dict[str, int]) -> np.ndarray:
    """Convert matrix to numpy array."""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = mapping[matrix[i][j]]  # type: ignore[call-overload]
    matrix_np = np.array([np.array(line, np.int8) for line in matrix])
    return matrix_np
