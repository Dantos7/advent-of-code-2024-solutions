from enum import Enum
import typer
import os
import re
import ast

class InstanceType(str, Enum):
    EXAMPLES = "examples"
    INPUTS = "inputs"


def first_part(instance: InstanceType, day: str):
    with open(f"data/{instance.value}/{day}.txt") as f:
        lines = f.readlines()

    nested_results = [extract_multiplication_results(line.strip()) for line in lines]
    flat_results = [x for xs in nested_results for x in xs]

    return sum(flat_results)
            

def extract_multiplication_results(line:str):
    matching_regex = "mul\([1-9]+[0-9]*,[1-9]+[0-9]*\)"
    matches = re.findall(matching_regex, line)
    return [compute_multiplication(mul) for mul in matches]

         
def compute_multiplication(str_mul: str) -> int:
    a,b = ast.literal_eval(str_mul.removeprefix("mul"))
    return a*b


def second_part(instance: InstanceType, day: str):
    pass


def main(instance: InstanceType):
    day = os.path.basename(__file__).removesuffix(".py")

    result = first_part(instance, day)
    print(result)

    # result = second_part(instance, day)
    # print(result)


if __name__ == "__main__":
    typer.run(main)