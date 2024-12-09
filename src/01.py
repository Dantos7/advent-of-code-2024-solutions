from collections import Counter

def first_part():
    with open("data/inputs/01.txt") as f:
        lines = f.readlines()

    first_vector = sorted([int(line.strip().split("   ")[0]) for line in lines])
    second_vector = sorted([int(line.strip().split("   ")[1]) for line in lines])

    result = 0
    for a, b in zip(first_vector, second_vector):
        result += abs(a-b)
    print(result)

first_part()

def second_part():
    with open("data/inputs/01.txt") as f:
        lines = f.readlines()

    first_vector = [int(line.strip().split("   ")[0]) for line in lines]
    second_vector = [int(line.strip().split("   ")[1]) for line in lines]
    counter_second = Counter(second_vector)

    result = 0
    for a in first_vector:
        result += a * counter_second[a]
    print(result)

second_part()