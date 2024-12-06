from enum import Enum
import typer
import os

class InstanceType(str, Enum):
    EXAMPLES = "examples"
    INPUTS = "inputs"


def first_part(instance: InstanceType, day: str):
    with open(f"data/{instance.value}/{day}.txt") as f:
        lines = f.readlines()

    matrix = []
    for line in lines:
        matrix.append([c for c in line.strip()])

    visited_positions = []
    i,j = find_guard_start_position(matrix)
    visited_positions.append((i,j))
    direction = "up"
    while (i < len(matrix) and i >= 0 and j < len(matrix[0]) and j >= 0):
        i, j, direction = compute_new_position(matrix, i, j, direction)
        if (i,j) not in visited_positions:
            visited_positions.append((i,j))

    count = len(visited_positions) - 1 # Remove last out of the matrix position

    return count
          

def find_guard_start_position(matrix: list[list[str]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == "^":
                return i,j


def compute_new_position(matrix, i, j, direction):
    if direction == "up":
        candidate_i, candidate_j = (i-1, j)
    elif direction == "down":
        candidate_i, candidate_j = (i+1, j)
    elif direction == "left":
        candidate_i, candidate_j = (i, j-1)
    elif direction == "right":
        candidate_i, candidate_j = (i, j+1)

    if not is_occupied(matrix, candidate_i, candidate_j):
        return candidate_i, candidate_j, direction
    else:
        direction = compute_new_direction(direction)
        return i,j,direction


def is_occupied(matrix, i, j):
    try:
        return matrix[i][j] == "#"
    except IndexError:
        return False


def compute_new_direction(direction):
    if direction == "up":
        return "right"
    if direction == "right":
        return "down"
    if direction == "down":
        return "left"
    if direction == "left":
        return "up"


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