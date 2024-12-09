"""Day 5: Print Queue."""

from pathlib import Path

import typer
from loguru import logger

from aoc import InstanceType, read_day_instance_lines


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 5."""
    lines = read_day_instance_lines(instance, day)

    i = 0
    for i in range(len(lines)):
        if lines[i] == "":
            break

    lines_first = lines[:i]
    lines_second = lines[i + 1 :]

    rules = parse_first_half(lines_first)
    updates = parse_second_half(lines_second)
    valid_updates = get_valid_updates(updates, rules)

    result = 0
    for i in valid_updates:
        upd = updates[i]
        middle = len(upd) // 2
        result += int(upd[middle])

    return result


def parse_first_half(lines_first: list[str]) -> dict[str, list[str]]:
    """Parse first half of the lines."""
    rules: dict[str, list[str]] = {}
    for line in lines_first:
        a, b = line.split("|")
        rules[a] = [*rules.get(a, []), b]

    return rules


def parse_second_half(lines_second: list[str]) -> list[list[str]]:
    """Parse second half of the lines."""
    return [line.split(",") for line in lines_second]


def get_valid_updates(updates: list[list[str]], rules: dict) -> list[int]:
    """Get valid updates."""
    valid_updates = []
    for i, line in enumerate(updates):
        is_update_valid = True
        max_j = len(line) - 1
        for j in range(max_j + 1):
            number_analyzed = line[max_j - j]
            for z in range(max_j - j):
                if number_analyzed in rules and line[z] in rules[number_analyzed]:
                    is_update_valid = False
                    break
            if not is_update_valid:
                break

        if is_update_valid:
            valid_updates.append(i)

    return valid_updates


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 5."""
    lines = read_day_instance_lines(instance, day)  # noqa: F841
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
