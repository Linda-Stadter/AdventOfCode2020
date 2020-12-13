input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines = [int(x.strip()) for x in input_lines]

    input_lines.append(0)
    return sorted(input_lines)


def part_one(input_lines):
    differences = {1: 0, 3: 1}

    for i in range(1, len(input_lines)):
        for k, v in differences.items():
            if input_lines[i] - k == input_lines[i-1]:
                differences[k] = v + 1

    return differences[1] * differences[3]


def part_two(input_lines):
    possibilities = [0, 0, 1]
    
    for i in range(1, len(input_lines)):
        for j in range(1, 4):
            if input_lines[i] - j == input_lines[i-1]:
                possibilities.extend((j-1)*[0])
                possibilities.append(sum(possibilities[-3:]))

    return possibilities[-1]


input_lines = read_input()
multiplied = part_one(input_lines)
print(multiplied)
possibilities = part_two(input_lines)
print(possibilities)
