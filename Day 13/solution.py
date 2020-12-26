import re
import math
input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines = [x.strip() for x in input_lines]

    return input_lines


def part_one(input_lines):
    timestamp = int(input_lines[0])
    bus_lines = re.findall("(\d+)", input_lines[1])
    next_lines = []

    for bus in bus_lines:
        next_lines.append((int(bus), math.ceil(timestamp/int(bus)) * int(bus)))

    next_lines.sort(key=lambda x: x[1])
    minutes = next_lines[0][1] - timestamp
    bus_id = next_lines[0][0]

    print(minutes * bus_id)


def part_two(input_lines):
    bus_lines = re.findall("([x,]*)(\d+)", input_lines[1])

    N = 1
    X = []
    old_offset = 0

    for offset, bus_id in bus_lines:
        N *= int(bus_id)

    for offset, bus_id in bus_lines[1:]:
        offset = [x for x in offset if x == 'x']

        b = int(bus_id) - (old_offset + len(offset) + 1)
        N_i = N // int(bus_id)
        x_i = pow(N_i, -1, int(bus_id))
        X.append(N_i * x_i * b)
        old_offset = (old_offset + len(offset) + 1)

    print(sum(X) % N)


input_lines = read_input()
part_one(input_lines)
part_two(input_lines)
