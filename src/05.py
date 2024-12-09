from enum import Enum
import typer
import os

class InstanceType(str, Enum):
    EXAMPLES = "examples"
    INPUTS = "inputs"


def first_part(instance: InstanceType, day: str):
    with open(f"data/{instance.value}/{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    i = 0
    for i in range(0, len(lines)):
        if lines[i] == "":
            break

    lines_first = lines[:i]
    lines_second = lines[i+1:]

    rules = parse_first_half(lines_first)
    updates = parse_second_half(lines_second)
    valid_updates = get_valid_updates(updates, rules)
    
    result = 0
    for i in valid_updates:
        upd = updates[i]
        middle = len(upd) // 2
        result += int(upd[middle])

    return result


def parse_first_half(lines_first:list[str]) -> dict:
    rules = {}
    for line in lines_first:
        a,b = line.split("|")
        rules[a] = rules.get(a, []) + [b] 

    return rules


def parse_second_half(lines_second:list[str]) -> list[list[str]]:
    return [line.split(",") for line in lines_second]


def get_valid_updates(updates:list[list[str]], rules:dict) -> list[int]:
    valid_updates = []
    for i, line in enumerate(updates):
        is_update_valid = True
        max_j = len(line) - 1
        for j in range(0,max_j+1):
            number_analyzed = line[max_j - j]
            for z in range(0, max_j - j):
                if number_analyzed in rules.keys() and line[z] in rules[number_analyzed]:
                    is_update_valid = False
                    break
            if not is_update_valid:
                break
        
        if is_update_valid:
            valid_updates.append(i)
    
    return valid_updates



def second_part(instance: InstanceType, day: str):
    with open(f"data/{instance.value}/{day}.txt") as f:
        lines = f.readlines()

    pass


def main(instance: InstanceType):
    day = os.path.basename(__file__).removesuffix(".py")

    result = first_part(instance, day)
    print(result)

    result = second_part(instance, day)
    print(result)


if __name__ == "__main__":
    typer.run(main)