import re
from collections import defaultdict
input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readline().split(',')

    return [int(x) for x in input_lines]


def memory_game(input_line, position):
    spoken_numbers = defaultdict(int)
    last_num = input_line[-1]

    for i, starting_numbers in enumerate(input_line):
        spoken_numbers[starting_numbers] = i + 1

    for i in range(len(input_line), position):
        if spoken_numbers[last_num] != 0:
            new_last_num = i - spoken_numbers[last_num]
            spoken_numbers[last_num] = i
            last_num = new_last_num
        else:
            spoken_numbers[last_num] = i
            last_num = 0

    return last_num


def part_one(input_line):
    print(memory_game(input_line, 2020))


def part_two(input_line):
    print(memory_game(input_line, 30000000))


input_line = read_input()
part_one(input_line)
part_two(input_line)
