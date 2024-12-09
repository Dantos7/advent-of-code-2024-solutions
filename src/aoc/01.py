"""Day 1: Historian Hysteria."""

from collections import Counter
from pathlib import Path

import typer
from loguru import logger

from aoc import InstanceType, read_day_instance_lines


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 1."""
    lines = read_day_instance_lines(instance, day)

    first_vector = sorted([int(line.split("   ")[0]) for line in lines])
    second_vector = sorted([int(line.split("   ")[1]) for line in lines])

    result = 0
    for a, b in zip(first_vector, second_vector, strict=False):
        result += abs(a - b)

    return result


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 1."""
    lines = read_day_instance_lines(instance, day)

    first_vector = [int(line.split("   ")[0]) for line in lines]
    second_vector = [int(line.split("   ")[1]) for line in lines]
    counter_second = Counter(second_vector)

    result = 0
    for a in first_vector:
        result += a * counter_second[a]

    return result


def main(instance: InstanceType) -> None:
    """Main function."""
    day = Path(__file__).name.removesuffix(".py")

    result = first_part(instance, day)
    logger.info(result)

    result = second_part(instance, day)
    logger.info(result)


if __name__ == "__main__":
    typer.run(main)
