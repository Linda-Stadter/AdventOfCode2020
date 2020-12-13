import re
input_path = "input.txt"
preamble_length = 25


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines = [int(x.strip()) for x in input_lines]

    return input_lines


def part_one(input_lines):
    preamble = input_lines[:preamble_length]

    for next_num in input_lines[preamble_length:]:
        preamble = check_validity(preamble, next_num)
        if not isinstance(preamble, list):
            return preamble


def check_validity(preamble, next_num):
    for num in preamble:
        if next_num - num in preamble and (next_num - num != num or preamble.count(num) > 1):
            preamble = preamble[1:]
            preamble.append(next_num)
            return preamble

    return next_num


def part_two(input_lines, invalid_number):
    for start in range(len(input_lines)):
        tmp = [input_lines[start], input_lines[start+1]]
        i = start + 2

        while sum(tmp) < invalid_number:
            tmp.append(input_lines[i])
            i += 1

        if sum(tmp) == invalid_number:
            return min(tmp)+max(tmp)


input_lines = read_input()
invalid_number = part_one(input_lines)
print(invalid_number)
encryption_weakness = part_two(input_lines, invalid_number)
print(encryption_weakness)
