"""Day 3: Mull It Over."""

import ast
import re
from pathlib import Path

import typer
from loguru import logger

from aoc import InstanceType, read_day_instance_lines


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 3."""
    lines = read_day_instance_lines(instance, day)

    nested_results = [extract_multiplication_results(line) for line in lines]
    flat_results = [x for xs in nested_results for x in xs]

    return sum(flat_results)


def extract_multiplication_results(line: str) -> list[int]:
    """Extract multiplication results from line."""
    matching_regex = r"mul\([1-9]+[0-9]*,[1-9]+[0-9]*\)"
    matches = re.findall(matching_regex, line)
    return [compute_multiplication(mul) for mul in matches]


def compute_multiplication(str_mul: str) -> int:
    """Compute multiplication."""
    a, b = ast.literal_eval(str_mul.removeprefix("mul"))
    return a * b


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 3."""
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
