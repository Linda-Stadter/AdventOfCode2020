import re
input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines = [x.strip() for x in input_lines]

    return input_lines


def part_one(input_lines):
    east = 0
    north = 0
    direction_index = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for line in input_lines:
        action, val = re.findall("([A-Z])(\d+)", line)[0]
        val = int(val)
        if action == "N":
            north += val
        elif action == "S":
            north -= val
        elif action == "E":
            east += val
        elif action == "W":
            east -= val
        elif action == "L":
            direction_index = (direction_index + (val // 90)) % 4
        elif action == "R":
            direction_index = (direction_index - (val // 90)) % 4
        elif action == "F":
            east += directions[direction_index][0] * val
            north += directions[direction_index][1] * val

    print(abs(east) + abs(north))


def part_two(input_lines):
    east = 0
    north = 0
    east_w = 10
    north_w = 1

    for line in input_lines:
        action, val = re.findall("([A-Z])(\d+)", line)[0]
        val = int(val)
        directions = [(east_w, north_w), (-north_w, east_w), (-east_w, -north_w), (north_w, -east_w)]
        if action == "N":
            north_w += val
        elif action == "S":
            north_w -= val
        elif action == "E":
            east_w += val
        elif action == "W":
            east_w -= val
        elif action == "L" or action == "R":
            direction_index = (val // 90) % 4
            if action == "R":
                direction_index = -direction_index
            east_w = directions[direction_index][0]
            north_w = directions[direction_index][1]
        elif action == "F":
            east += east_w * val
            north += north_w * val

    print(abs(east) + abs(north))


input_lines = read_input()
part_one(input_lines)
part_two(input_lines)