"""Day 6: Guard Gallivant."""

from pathlib import Path

import typer
from loguru import logger

from aoc import InstanceType, read_day_instance_lines


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 6."""
    lines = read_day_instance_lines(instance, day)
    equations = parse_equations(lines)
    sum_results = 0
    for result, terms in equations:
        if is_valid(result, terms[1:], terms[0]):
            sum_results += result

    return sum_results


def parse_equations(lines: list[str]) -> list[tuple[int, list[int]]]:
    """Parse equations."""
    equations = []
    for line in lines:
        result_str, terms_str = line.split(": ")
        result = int(result_str)
        terms = [int(t) for t in terms_str.split(" ")]
        equations.append((result, terms))

    return equations


def is_valid(result: int, terms: list[int], cumulative_value: int) -> bool:
    """Recursive function checking if the equation can be valid with at least one possible operands assignment."""
    if cumulative_value > result:
        return False
    if len(terms) == 0:
        return cumulative_value == result
    else:
        is_valid_plus = is_valid(result, terms[1:], cumulative_value + terms[0])
        is_valid_times = is_valid(result, terms[1:], cumulative_value * terms[0])
        return is_valid_plus or is_valid_times


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 6."""
    lines = read_day_instance_lines(instance, day)
    equations = parse_equations(lines)
    sum_results = 0
    for result, terms in equations:
        if is_valid_2(result, terms[1:], terms[0]):
            sum_results += result

    return sum_results


def is_valid_2(result: int, terms: list[int], cumulative_value: int) -> bool:
    """Recursive function checking if the equation can be valid with at least one possible operands assignment."""
    if cumulative_value > result:
        return False
    if len(terms) == 0:
        return cumulative_value == result
    else:
        is_valid_plus = is_valid_2(result, terms[1:], cumulative_value + terms[0])
        is_valid_times = is_valid_2(result, terms[1:], cumulative_value * terms[0])
        is_valid_concat = is_valid_2(result, terms[1:], concat(cumulative_value, terms[0]))
        return is_valid_plus or is_valid_times or is_valid_concat


def concat(a: int, b: int) -> int:
    """Concatenate two integers."""
    return int(str(a) + str(b))


def main(instance: InstanceType) -> None:
    """Main function."""
    day = Path(__file__).name.removesuffix(".py")

    result = first_part(instance, day)
    logger.info(f"1st:\t{result}")

    result = second_part(instance, day)
    logger.info(f"2nd:\t{result}")


if __name__ == "__main__":
    typer.run(main)
