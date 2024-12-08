"""Day 8: Resonant Collinearity."""

from pathlib import Path

import typer
from loguru import logger

from aoc import InstanceType, read_day_instance_matrix


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 8."""
    matrix = read_day_instance_matrix(instance, day)
    frequencies_locations: dict[str, list[tuple[int, int]]] = get_frequencies_locations(matrix)
    antinodes = set()
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1
    for locations in frequencies_locations.values():
        antinodes_freq = get_antinodes_locations(locations, max_i, max_j)
        antinodes.update(antinodes_freq)

    return len(antinodes)


def get_frequencies_locations(matrix: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    """Get frequencies locations."""
    frequencies_locations: dict[str, list[tuple[int, int]]] = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == ".":
                continue
            frequency = matrix[i][j]
            frequencies_locations[frequency] = [*frequencies_locations.get(frequency, []), (i, j)]

    return frequencies_locations


def get_antinodes_locations(locations: list[tuple[int, int]], max_i: int, max_j: int) -> set[tuple[int, int]]:
    """Get antinodes locations."""
    all_antinodes = set()
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            antinodes_couple = get_antinodes_couple(locations[i], locations[j], max_i, max_j)
            all_antinodes.add(antinodes_couple[0])
            all_antinodes.add(antinodes_couple[1])

    # Remove antinodes that are out of the matrix
    all_antinodes.discard(None)

    return all_antinodes  # type: ignore[return-value]


def get_antinodes_couple(
    loc_1: tuple[int, int],
    loc_2: tuple[int, int],
    max_i: int,
    max_j: int,
) -> tuple[tuple[int, int] | None, tuple[int, int] | None]:
    """Get antinode for the given couple of locations."""
    i_diff = loc_2[0] - loc_1[0]
    j_diff = loc_2[1] - loc_1[1]
    antinode_i_1 = loc_1[0] - i_diff
    antinode_j_1 = loc_1[1] - j_diff
    antinode_i_2 = loc_2[0] + i_diff
    antinode_j_2 = loc_2[1] + j_diff
    if 0 <= antinode_i_1 <= max_i and 0 <= antinode_j_1 <= max_j:  # noqa: SIM108
        antinode_1 = (antinode_i_1, antinode_j_1)
    else:
        antinode_1 = None
    if 0 <= antinode_i_2 <= max_i and 0 <= antinode_j_2 <= max_j:  # noqa: SIM108
        antinode_2 = (antinode_i_2, antinode_j_2)
    else:
        antinode_2 = None
    return (antinode_1, antinode_2)


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 8."""
    matrix = read_day_instance_matrix(instance, day)
    frequencies_locations: dict[str, list[tuple[int, int]]] = get_frequencies_locations(matrix)
    antinodes = set()
    max_i = len(matrix) - 1
    max_j = len(matrix[0]) - 1
    for locations in frequencies_locations.values():
        antinodes_freq = get_antinodes_locations_line(locations, max_i, max_j)
        antinodes.update(antinodes_freq)
    return len(antinodes)


def get_antinodes_locations_line(locations: list[tuple[int, int]], max_i: int, max_j: int) -> set[tuple[int, int]]:
    """Get antinodes locations (line)."""
    all_antinodes = set()
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            antinodes_couple_line = get_antinodes_couple_line(locations[i], locations[j], max_i, max_j)
            all_antinodes.update(antinodes_couple_line)

    return all_antinodes


def get_antinodes_couple_line(
    loc_1: tuple[int, int],
    loc_2: tuple[int, int],
    max_i: int,
    max_j: int,
) -> set[tuple[int, int]]:
    """Get antinodes for the given couple of locations (line)."""
    antinodes_line = set()
    antinodes_line.add(loc_1)
    antinodes_line.add(loc_2)

    i_diff = loc_2[0] - loc_1[0]
    j_diff = loc_2[1] - loc_1[1]

    antinode_i_1 = loc_1[0] - i_diff
    antinode_j_1 = loc_1[1] - j_diff

    while 0 <= antinode_i_1 <= max_i and 0 <= antinode_j_1 <= max_j:
        antinodes_line.add((antinode_i_1, antinode_j_1))
        antinode_i_1 -= i_diff
        antinode_j_1 -= j_diff

    antinode_i_2 = loc_2[0] + i_diff
    antinode_j_2 = loc_2[1] + j_diff
    while 0 <= antinode_i_2 <= max_i and 0 <= antinode_j_2 <= max_j:
        antinodes_line.add((antinode_i_2, antinode_j_2))
        antinode_i_2 += i_diff
        antinode_j_2 += j_diff

    return antinodes_line


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
