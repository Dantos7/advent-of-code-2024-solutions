"""Day 2: Red-Nosed Reports."""

from pathlib import Path

import typer
from loguru import logger

from aoc import InstanceType, read_day_instance_lines


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 2."""
    lines = read_day_instance_lines(instance, day)

    safe_reports = 0
    for line in lines:
        report = [int(n) for n in line.split(" ")]

        if is_safe(report):
            safe_reports += 1

    return safe_reports


def is_safe(report: list[int]) -> bool:
    """Check if the report is safe."""
    report_direction = None
    for i in range(len(report) - 1):
        difference = report[i] - report[i + 1]
        if difference == 0:
            return False
        elif difference > 0:
            if report_direction is None:
                report_direction = "ascending"
            elif report_direction == "ascending":
                pass
            else:
                return False
        elif report_direction is None:
            report_direction = "descending"
        elif report_direction == "descending":
            pass
        else:
            return False

        if not (1 <= abs(difference) <= 3):
            return False

    return True


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 2."""
    lines = read_day_instance_lines(instance, day)

    safe_reports = 0
    for _i, line in enumerate(lines):
        report = [int(n) for n in line.split(" ")]

        if is_safe_with_problem_dampener(report):
            safe_reports += 1

    return safe_reports


def is_safe_with_problem_dampener(report: list[int]) -> bool:
    """Check if the report is safe with a problem dampener."""
    i = 0
    safe = is_safe(report)
    while i < len(report) and not safe:
        safe = is_safe(report[:i] + report[i + 1 :])
        i += 1

    return safe


def main(instance: InstanceType) -> None:
    """Main function."""
    day = Path(__file__).name.removesuffix(".py")

    result = first_part(instance, day)
    logger.info(result)

    result = second_part(instance, day)
    logger.info(result)


if __name__ == "__main__":
    typer.run(main)
