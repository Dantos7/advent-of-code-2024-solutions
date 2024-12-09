"""Day 9: Disk Fragmenter."""

from pathlib import Path

import typer
from loguru import logger

from aoc import InstanceType, read_day_instance_lines


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 9."""
    line = read_day_instance_lines(instance, day)[0]
    line_list = list(line)
    explicit_line = convert_to_explicit(line_list)
    rearranged_line = move_blocks_from_right(explicit_line)
    checksum = compute_checksum(rearranged_line)
    return checksum


def convert_to_explicit(line_list: list[str]) -> list[str]:
    """Convert the compressed line to explicit line of IDs and empty spaces."""
    file = True
    file_id = 0
    explicit_line = []
    for c in line_list:
        repetitions = int(c)
        if file:
            explicit_line += [str(file_id)] * repetitions
            file = False
            file_id += 1
        else:
            explicit_line += ["."] * repetitions
            file = True
    return explicit_line


def move_blocks_from_right(explicit_line: list[str]) -> list[str]:
    """Move blocks from right to left."""
    i = 0
    j = len(explicit_line) - 1
    while i < j:
        # Move i pointer to the first empty space
        while explicit_line[i] != "." and i < j:
            i += 1
        # Move j pointer to the first non-empty space
        while explicit_line[j] == "." and i < j:
            j -= 1

        if explicit_line[i] == "." and explicit_line[j] != "." and i != j:
            explicit_line[i] = explicit_line[j]
            explicit_line[j] = "."
        j -= 1
        i += 1

    return explicit_line


def compute_checksum(rearranged_line: list[str]) -> int:
    """Compute the checksum."""
    ranked_scores = [i * int(c) for i, c in enumerate(rearranged_line) if c != "."]
    return sum(ranked_scores)


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 9."""
    line = read_day_instance_lines(instance, day)[0]
    line_list = list(line)
    explicit_line = convert_to_explicit(line_list)
    rearranged_line = move_files_from_right(explicit_line)
    checksum = compute_checksum(rearranged_line)
    return checksum


def move_files_from_right(explicit_line: list[str]) -> list[str]:
    """Move files from right to left."""
    i = 0
    j = len(explicit_line) - 1
    already_moved = set()
    while i < j:
        # Move j pointer to the first non-empty space
        while explicit_line[j] == "." and i < j:
            j -= 1
        j_size = 0
        j_id = explicit_line[j]
        while explicit_line[j - j_size] == j_id:
            j_size += 1
        if j_id in already_moved:
            j -= j_size
            continue

        # Move i pointer to the first empty space
        while explicit_line[i] != "." and i < j:
            i += 1

        # Try every possible size of empty space
        i_trial = i
        while i_trial < j:
            # Compute size of empty space
            i_size = 0
            while explicit_line[i_trial + i_size] == ".":
                i_size += 1

            if explicit_line[i_trial] == "." and explicit_line[j] != "." and i_trial != j and i_size >= j_size:
                for k in range(j_size):
                    explicit_line[i_trial + k] = explicit_line[j - k]
                    explicit_line[j - k] = "."
                i_trial += j_size
                already_moved.add(j_id)
                break
            if j_id in already_moved:
                break

            i_trial += i_size + 1
            # Move i_trial pointer to the next empty space
            while explicit_line[i_trial] != "." and i_trial < j:
                i_trial += 1

        j -= j_size
        i = 0

    return explicit_line


def main(instance: InstanceType) -> None:
    """Main function."""
    day = Path(__file__).name.removesuffix(".py")

    result = first_part(instance, day)
    logger.info(f"1st:\t{result}")

    result = second_part(instance, day)
    logger.info(f"2nd:\t{result}")


if __name__ == "__main__":
    typer.run(main)
