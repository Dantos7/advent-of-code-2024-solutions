"""Day 6: Guard Gallivant."""

from pathlib import Path

import numpy as np
import typer
from loguru import logger

from aoc import InstanceType, convert_matrix_to_numpy, read_day_instance_matrix


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 6."""
    matrix = read_day_instance_matrix(instance, day)
    visited_positions = get_visited_positions(matrix, obstacle_symbol="#", guard_symbol="^")
    count = len(visited_positions)

    return count


def get_visited_positions(matrix: list[list[str]], obstacle_symbol: str | int, guard_symbol: str | int) -> set[tuple[int, int]]:
    """Compute the guard path."""
    visited_positions = set()
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1
    i, j = find_guard_start_position(matrix, guard_symbol)
    visited_positions.add((i, j))
    direction = "up"
    while i < len(matrix) and i >= 0 and j < len(matrix[0]) and j >= 0:
        i, j, direction = compute_new_position(matrix, i, j, direction, max_i, max_j, obstacle_symbol)
        if (i, j) not in visited_positions:
            visited_positions.add((i, j))
    visited_positions.remove((i, j))  # Remove last out of the matrix position
    return visited_positions


def find_guard_start_position(matrix: list[list[str]] | np.ndarray, guard_symbol: str | int) -> tuple[int, int]:  # type: ignore[return]
    """Find the guard start position."""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == guard_symbol:
                return i, j


def compute_new_position(
    matrix: list[list[str]],
    i: int,
    j: int,
    direction: str,
    max_i: int,
    max_j: int,
    obstacle_symbol: str | int,
) -> tuple[int, int, str]:
    """Compute the new position."""
    if direction == "up":
        candidate_i, candidate_j = (i - 1, j)
    elif direction == "down":
        candidate_i, candidate_j = (i + 1, j)
    elif direction == "left":
        candidate_i, candidate_j = (i, j - 1)
    elif direction == "right":
        candidate_i, candidate_j = (i, j + 1)

    if not is_occupied(matrix, candidate_i, candidate_j, max_i, max_j, obstacle_symbol):
        return candidate_i, candidate_j, direction
    else:
        direction = compute_new_direction(direction)
        return i, j, direction


def is_occupied(matrix: list[list[str]] | np.ndarray, i: int, j: int, max_i: int, max_j: int, obstacle_symbol: str | int) -> bool:
    """Check if the position is occupied by an obstacle."""
    if 0 <= i <= max_i and 0 <= j <= max_j:
        return matrix[i][j] == obstacle_symbol
    else:
        return False


def compute_new_direction(direction: str) -> str:
    """Compute the new direction (90° right rotation)."""
    new_direction = {"up": "right", "right": "down", "down": "left", "left": "up"}
    return new_direction[direction]


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 6."""
    matrix = read_day_instance_matrix(instance, day)
    count = second_part_core(matrix, obstacle_symbol="#", free_symbol=".", guard_symbol="^")
    return count


def second_part_numeric(instance: InstanceType, day: str) -> int:
    """Second part of day 6."""
    matrix = convert_matrix_to_numpy(read_day_instance_matrix(instance, day), {"^": -1, "#": 1, ".": 0})
    count = second_part_core(matrix, obstacle_symbol=1, free_symbol=0, guard_symbol=-1)
    return count


def second_part_core(
    matrix: list[list[str]] | np.ndarray,
    obstacle_symbol: str | int,
    free_symbol: str | int,
    guard_symbol: str | int,
) -> int:
    """Core part of the second day solution code in common between string and numeric approaches."""
    # Get visited positions in the standard non-cyclic path
    visited_positions = get_visited_positions(matrix, obstacle_symbol, guard_symbol)
    start_i, start_j = find_guard_start_position(matrix, guard_symbol)
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1
    cycle_obstacles = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Don't try to put an obstacle where there is already one or where the guard is starting
            if (i, j) not in visited_positions or (i, j) == (start_i, start_j):
                continue
            # Put obstacle
            matrix[i][j] = obstacle_symbol  # type: ignore[assignment]
            if has_cycle(matrix, start_i, start_j, max_i, max_j, obstacle_symbol):
                cycle_obstacles.append((i, j))
            # Restore the matrix
            matrix[i][j] = free_symbol  # type: ignore[assignment]

    return len(cycle_obstacles)


def has_cycle(matrix: list[list[str]], i: int, j: int, max_i: int, max_j: int, obstacle_symbol: str | int) -> bool:
    """Checks if the guard path has a cycle. It does this by checking if the guard passes twice through the same position with the same direction."""
    visited_positions_with_direction = set()
    direction = "up"
    visited_positions_with_direction.add((i, j, direction))
    while i < len(matrix) and i >= 0 and j < len(matrix[0]) and j >= 0:
        i, j, direction = compute_new_position(matrix, i, j, direction, max_i, max_j, obstacle_symbol)
        if (i, j, direction) in visited_positions_with_direction:
            return True
        else:
            visited_positions_with_direction.add((i, j, direction))

    return False


def main(instance: InstanceType) -> None:
    """Main function."""
    day = Path(__file__).name.removesuffix(".py")

    result = first_part(instance, day)
    logger.info(result)

    result = second_part(instance, day)
    logger.info(f"2ND CHAR:\t{result}")

    result = second_part_numeric(instance, day)
    logger.info(f"2ND NUMERIC:\t{result}")


if __name__ == "__main__":
    typer.run(main)
