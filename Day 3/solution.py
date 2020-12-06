input_path = "input.txt"


def check_trees(slope_x, slope_y):

    trees = 0
    pos_x = 0

    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines = [x.strip() for x in input_lines]

    for line in input_lines[::slope_y]:
        line = list(line)
        if line[pos_x % len(line)] == "#":
            trees += 1
        pos_x += slope_x

    return trees


def part_one():

    print(check_trees(3, 1))


def part_two():

    print(check_trees(1, 1) * check_trees(3, 1) *
          check_trees(5, 1) * check_trees(7, 1) * check_trees(1, 2))


part_one()
part_two()
