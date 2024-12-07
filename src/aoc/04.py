"""Day 4: Ceres Search."""

from pathlib import Path

import typer
from loguru import logger

from aoc import InstanceType, read_day_instance_matrix


def first_part(instance: InstanceType, day: str) -> int:
    """First part of day 4."""
    matrix = read_day_instance_matrix(instance, day)

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count += int(is_xmas_right(matrix, i, j))
            count += int(is_xmas_left(matrix, i, j))
            count += int(is_xmas_down(matrix, i, j))
            count += int(is_xmas_up(matrix, i, j))
            count += int(is_xmas_right_up(matrix, i, j))
            count += int(is_xmas_right_down(matrix, i, j))
            count += int(is_xmas_left_up(matrix, i, j))
            count += int(is_xmas_left_down(matrix, i, j))

    return count


def is_xmas_right(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word XMAS is in the right direction."""
    if j > (len(matrix[0]) - 4):
        return False
    return matrix[i][j] == "X" and matrix[i][j + 1] == "M" and matrix[i][j + 2] == "A" and matrix[i][j + 3] == "S"


def is_xmas_left(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word XMAS is in the left direction."""
    if j > (len(matrix[0]) - 4):
        return False
    return matrix[i][j] == "S" and matrix[i][j + 1] == "A" and matrix[i][j + 2] == "M" and matrix[i][j + 3] == "X"


def is_xmas_down(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word XMAS is in the down direction."""
    if i > (len(matrix) - 4):
        return False
    return matrix[i][j] == "X" and matrix[i + 1][j] == "M" and matrix[i + 2][j] == "A" and matrix[i + 3][j] == "S"


def is_xmas_up(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word XMAS is in the up direction."""
    if i > (len(matrix) - 4):
        return False
    return matrix[i][j] == "S" and matrix[i + 1][j] == "A" and matrix[i + 2][j] == "M" and matrix[i + 3][j] == "X"


def is_xmas_right_up(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word XMAS is in the right up direction."""
    if i > (len(matrix) - 4) or j > (len(matrix[0]) - 4):
        return False
    return matrix[i][j] == "X" and matrix[i + 1][j + 1] == "M" and matrix[i + 2][j + 2] == "A" and matrix[i + 3][j + 3] == "S"


def is_xmas_left_down(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word XMAS is in the left down direction."""
    if i > (len(matrix) - 4) or j > (len(matrix[0]) - 4):
        return False
    return matrix[i][j] == "S" and matrix[i + 1][j + 1] == "A" and matrix[i + 2][j + 2] == "M" and matrix[i + 3][j + 3] == "X"


def is_xmas_right_down(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word XMAS is in the right down direction."""
    if i < 3 or j > (len(matrix[0]) - 4):
        return False
    return matrix[i][j] == "X" and matrix[i - 1][j + 1] == "M" and matrix[i - 2][j + 2] == "A" and matrix[i - 3][j + 3] == "S"


def is_xmas_left_up(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word XMAS is in the left up direction."""
    if i < 3 or j > (len(matrix[0]) - 4):
        return False
    return matrix[i][j] == "S" and matrix[i - 1][j + 1] == "A" and matrix[i - 2][j + 2] == "M" and matrix[i - 3][j + 3] == "X"


def second_part(instance: InstanceType, day: str) -> int:
    """Second part of day 4."""
    matrix = read_day_instance_matrix(instance, day)

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count += int(is_x_mas_1(matrix, i, j))
            count += int(is_x_mas_2(matrix, i, j))
            count += int(is_x_mas_3(matrix, i, j))
            count += int(is_x_mas_4(matrix, i, j))

    return count


def is_x_mas_1(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word X-MAS is found (1st option)."""
    if i < 1 or j > (len(matrix[0]) - 2) or i > (len(matrix) - 2) or j < 1:
        return False
    return (
        matrix[i][j] == "A"
        and matrix[i - 1][j - 1] == "S"
        and matrix[i + 1][j + 1] == "M"
        and matrix[i + 1][j - 1] == "M"
        and matrix[i - 1][j + 1] == "S"
    )


def is_x_mas_2(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word X-MAS is found (2nd option)."""
    if i < 1 or j > (len(matrix[0]) - 2) or i > (len(matrix) - 2) or j < 1:
        return False
    return (
        matrix[i][j] == "A"
        and matrix[i - 1][j - 1] == "M"
        and matrix[i + 1][j + 1] == "S"
        and matrix[i + 1][j - 1] == "M"
        and matrix[i - 1][j + 1] == "S"
    )


def is_x_mas_3(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word X-MAS is found (3rd option)."""
    if i < 1 or j > (len(matrix[0]) - 2) or i > (len(matrix) - 2) or j < 1:
        return False
    return (
        matrix[i][j] == "A"
        and matrix[i - 1][j - 1] == "M"
        and matrix[i + 1][j + 1] == "S"
        and matrix[i + 1][j - 1] == "S"
        and matrix[i - 1][j + 1] == "M"
    )


def is_x_mas_4(matrix: list[list[str]], i: int, j: int) -> bool:
    """Check if the word X-MAS is found (4th option)."""
    if i < 1 or j > (len(matrix[0]) - 2) or i > (len(matrix) - 2) or j < 1:
        return False
    return (
        matrix[i][j] == "A"
        and matrix[i - 1][j - 1] == "S"
        and matrix[i + 1][j + 1] == "M"
        and matrix[i + 1][j - 1] == "S"
        and matrix[i - 1][j + 1] == "M"
    )


def main(instance: InstanceType) -> None:
    """Main function."""
    day = Path(__file__).name.removesuffix(".py")

    result = first_part(instance, day)
    logger.info(result)

    result = second_part(instance, day)
    logger.info(result)


if __name__ == "__main__":
    typer.run(main)
