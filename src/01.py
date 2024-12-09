with open("data/inputs/01.txt") as f:
    lines = f.readlines()

first_vector = sorted([int(line.strip().split("   ")[0]) for line in lines])
second_vector = sorted([int(line.strip().split("   ")[1]) for line in lines])

result = 0
for a, b in zip(first_vector, second_vector):
    result += abs(a-b)
print(result)
