from enum import Enum
import typer
import os

class InstanceType(str, Enum):
    EXAMPLES = "examples"
    INPUTS = "inputs"


def first_part(instance: InstanceType, day: str):
    with open(f"data/{instance.value}/{day}.txt") as f:
        lines = f.readlines()

    safe_reports = 0
    for line in lines:
        report = [int(n) for n in line.strip().split(" ")]
        
        if is_safe(report):
            safe_reports += 1

    return safe_reports


def is_safe(report: list[int]) -> bool:
    report_direction = None
    for i in range(0, len(report) -1):
        difference = report[i] - report[i+1]
        if difference == 0:
            return False
        elif difference > 0:
            if report_direction is None:
                report_direction = "ascending"
            elif report_direction == "ascending":
                pass
            else:
                return False
        else:
            if report_direction is None:
                report_direction = "descending"
            elif report_direction == "descending":
                pass
            else:
                return False            

        if not (1 <= abs(difference) <= 3):
            return False
        
    return True
            

def second_part(instance: InstanceType, day: str):
    with open(f"data/{instance.value}/{day}.txt") as f:
        lines = f.readlines()

    safe_reports = 0
    for _i, line in enumerate(lines):
        report = [int(n) for n in line.strip().split(" ")]
        
        if is_safe_with_problem_dampener(report):
            safe_reports += 1

    return safe_reports


def is_safe_with_problem_dampener(report: list[int]) -> bool:
    i = 0
    safe = is_safe(report)
    while i < len(report) and not safe:
        safe = is_safe(report[:i] + report[i+1:])
        i+=1

    return safe


def main(instance: InstanceType):
    day = os.path.basename(__file__).removesuffix(".py")

    result = first_part(instance, day)
    print(result)

    result = second_part(instance, day)
    print(result)


if __name__ == "__main__":
    typer.run(main)