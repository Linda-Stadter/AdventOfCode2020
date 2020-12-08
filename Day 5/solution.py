input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines.append("\n")
        input_lines = [x.strip() for x in input_lines]
    return input_lines


def binary_space_search(line, lower_key):
    min_row = 0
    max_row = 2**len(line) - 1
    for c in line[:]:
        mid = (min_row + max_row) // 2
        if c == lower_key:
            max_row = mid
        else:
            min_row = mid + 1
    return min_row


def part_one():
    all_ids = []
    input_lines = read_input()

    for line in input_lines:
        row = binary_space_search(line[:7], "F")
        col = binary_space_search(line[7:], "L")
        all_ids.append(row * 8 + col)

    return all_ids


def part_two():
    ids = part_one()
    possible = range(127*8+7)
    missing = list(set(possible) - set(ids))
    missing = sorted(missing)

    for i in range(1, len(missing)-1):
        if missing[i-1]+1 != missing[i] and missing[i]+1 != missing[i+1]:
            print(missing[i])


ids = part_one()
print(max(ids))
part_two()
