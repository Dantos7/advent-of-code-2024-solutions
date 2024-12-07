"""Day 6: Guard Gallivant."""

from pathlib import Path

import typer
from loguru import logger

from aoc import InstanceType, read_day_instance_matrix


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 6."""
    matrix = read_day_instance_matrix(instance, day)

    visited_positions = []
    i, j = find_guard_start_position(matrix)
    visited_positions.append((i, j))
    direction = "up"
    while i < len(matrix) and i >= 0 and j < len(matrix[0]) and j >= 0:
        i, j, direction = compute_new_position(matrix, i, j, direction)
        if (i, j) not in visited_positions:
            visited_positions.append((i, j))

    count = len(visited_positions) - 1  # Remove last out of the matrix position

    return count


def find_guard_start_position(matrix: list[list[str]]) -> tuple[int, int]:  # type: ignore[return]
    """Find the guard start position."""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^":
                return i, j


def compute_new_position(matrix: list[list[str]], i: int, j: int, direction: str) -> tuple[int, int, str]:
    """Compute the new position."""
    if direction == "up":
        candidate_i, candidate_j = (i - 1, j)
    elif direction == "down":
        candidate_i, candidate_j = (i + 1, j)
    elif direction == "left":
        candidate_i, candidate_j = (i, j - 1)
    elif direction == "right":
        candidate_i, candidate_j = (i, j + 1)

    if not is_occupied(matrix, candidate_i, candidate_j):
        return candidate_i, candidate_j, direction
    else:
        direction = compute_new_direction(direction)
        return i, j, direction


def is_occupied(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the position is occupied by an obstacle."""
    try:
        return matrix[i][j] == "#"
    except IndexError:
        return False


def compute_new_direction(direction: str) -> str:
    """Compute the new direction (90° right rotation)."""
    new_direction = {"up": "right", "right": "down", "down": "left", "left": "up"}
    return new_direction[direction]


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 6."""
    matrix = read_day_instance_matrix(instance, day)  # noqa: F841
    return 0


def main(instance: InstanceType) -> None:
    """Main function."""
    day = Path(__file__).name.removesuffix(".py")

    result = first_part(instance, day)
    logger.info(result)

    result = second_part(instance, day)
    logger.info(result)


if __name__ == "__main__":
    typer.run(main)
