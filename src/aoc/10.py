"""Day 10: Hoof It."""

# ruff: noqa: PLW0602 PLW0603

from pathlib import Path

import typer
from loguru import logger

from aoc import InstanceType, read_day_instance_matrix

# ! Yes, I am ashamed for how I have implemented recursion

all_paths: list[list[tuple[int, int]]] = []
found_ends: set[tuple[int, int]] = set()


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 10."""
    matrix = read_day_instance_matrix(instance, day)
    matrix = convert_matrix_to_int(matrix)
    trailheads = get_trailheads(matrix)
    count = 0
    global all_paths
    global found_ends
    for trailhead in trailheads:
        compute_ascending_paths_distinct_end(matrix, trailhead, [])
        all_paths = [p for p in all_paths if p is not None]
        count_paths = len(all_paths)
        all_paths = []
        found_ends = set()
        count += count_paths

    return count


def convert_matrix_to_int(matrix: list[list[str]]) -> list[list[int]]:
    """Convert matrix to int."""
    return [[int(cell) for cell in row] for row in matrix]


def get_trailheads(matrix: list[list[int]]) -> list[tuple[int, int]]:
    """Get frequencies locations."""
    return [(i, j) for j in range(len(matrix[0])) for i in range(len(matrix)) if matrix[i][j] == 0]


def compute_ascending_paths_distinct_end(
    matrix: list[list[int]],
    trailhead: tuple[int, int],
    preceding_path: list[tuple[int, int]],
) -> None:
    """Compute ascending paths."""
    global all_paths
    global found_ends
    path = [*preceding_path, trailhead]
    i, j = trailhead
    current_value = matrix[i][j]
    if i + 1 < len(matrix) and matrix[i + 1][j] == (current_value + 1):
        compute_ascending_paths_distinct_end(matrix, (i + 1, j), path)
    if i - 1 >= 0 and matrix[i - 1][j] == (current_value + 1):
        compute_ascending_paths_distinct_end(matrix, (i - 1, j), path)
    if j + 1 < len(matrix[0]) and matrix[i][j + 1] == (current_value + 1):
        compute_ascending_paths_distinct_end(matrix, (i, j + 1), path)
    if j - 1 >= 0 and matrix[i][j - 1] == (current_value + 1):
        compute_ascending_paths_distinct_end(matrix, (i, j - 1), path)
    if current_value == 9 and (i, j) not in found_ends:
        found_ends.add((i, j))
        all_paths.append(path)


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 10."""
    matrix = read_day_instance_matrix(instance, day)
    matrix = convert_matrix_to_int(matrix)
    trailheads = get_trailheads(matrix)
    count = 0
    global all_paths
    global found_ends
    for trailhead in trailheads:
        compute_ascending_unique_paths(matrix, trailhead, [])
        all_paths = [p for p in all_paths if p is not None]
        count_paths = len(all_paths)
        all_paths = []
        found_ends = set()
        count += count_paths

    return count


def compute_ascending_unique_paths(
    matrix: list[list[int]],
    trailhead: tuple[int, int],
    preceding_path: list[tuple[int, int]],
) -> None:
    """Compute ascending paths."""
    global all_paths
    path = [*preceding_path, trailhead]
    i, j = trailhead
    current_value = matrix[i][j]
    if i + 1 < len(matrix) and matrix[i + 1][j] == (current_value + 1):
        compute_ascending_unique_paths(matrix, (i + 1, j), path)
    if i - 1 >= 0 and matrix[i - 1][j] == (current_value + 1):
        compute_ascending_unique_paths(matrix, (i - 1, j), path)
    if j + 1 < len(matrix[0]) and matrix[i][j + 1] == (current_value + 1):
        compute_ascending_unique_paths(matrix, (i, j + 1), path)
    if j - 1 >= 0 and matrix[i][j - 1] == (current_value + 1):
        compute_ascending_unique_paths(matrix, (i, j - 1), path)
    if current_value == 9:
        all_paths.append(path)


def main(instance: InstanceType) -> None:
    """Main function."""
    day = Path(__file__).name.removesuffix(".py")

    logger.info(f"DAY:\t{day}")

    result = first_part(instance, day)
    logger.info(f"1st:\t{result}")

    result = second_part(instance, day)
    logger.info(f"2nd:\t{result}")


if __name__ == "__main__":
    typer.run(main)
