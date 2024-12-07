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
    lines = read_day_instance_lines(instance, day)
    is_enabled = True
    all_results = []

    for line in lines:
        mul_results, is_enabled = extract_multiplication_results_2(line, is_enabled)
        all_results += mul_results

    return sum(all_results)


def extract_multiplication_results_2(line: str, is_enabled: bool) -> tuple[list[int], bool]:
    """Extract multiplication results from line (taking care of do and don't)."""
    running_sequence = ""
    matching_regex = r"mul\([1-9]+[0-9]*,[1-9]+[0-9]*\)"
    mul_results = []
    for c in line:
        running_sequence += c
        if c not in ["d", "o", "n", "'", "t", "(", ")", "m", "u", "l", ",", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            running_sequence = ""
            continue
        if not ("do()".startswith(running_sequence) or "don't()".startswith(running_sequence) or match_mul_regex_start(running_sequence)):
            running_sequence = ""
            continue
        if running_sequence == "do()":
            is_enabled = True
            running_sequence = ""
        elif running_sequence == "don't()":
            is_enabled = False
            running_sequence = ""
        elif re.match(matching_regex, running_sequence):
            if is_enabled:
                mul_results.append(compute_multiplication(running_sequence))
            running_sequence = ""

    return mul_results, is_enabled


def match_mul_regex_start(running_sequence: str) -> bool:
    """Check if running sequence matches the start of the mul regex."""
    if running_sequence in ("m", "mu", "mul", "mul("):
        return True
    if re.match(r"^mul\([1-9]+[0-9]*$", running_sequence):
        return True
    if re.match(r"^mul\([1-9]+[0-9]*,$", running_sequence):
        return True
    if re.match(r"^mul\([1-9]+[0-9]*,[1-9]+[0-9]*$", running_sequence):
        return True
    return bool(re.match(r"^mul\([1-9]+[0-9]*,[1-9]+[0-9]*\)$", running_sequence))


def main(instance: InstanceType) -> None:
    """Main function."""
    day = Path(__file__).name.removesuffix(".py")

    result = first_part(instance, day)
    logger.info(result)

    result = second_part(instance, day)
    logger.info(result)


if __name__ == "__main__":
    typer.run(main)
