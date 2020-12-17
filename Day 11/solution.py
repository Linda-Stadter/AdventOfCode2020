input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines = [list(x.strip()) for x in input_lines]

    return input_lines


def get_neighbors_adjacent(input_lines, y, x):
    max_y = len(input_lines)
    max_x = len(input_lines[0])
 
    return [(row, column) for row in range(y-1, y+2) for column in range(x-1, x+2)
            if (0 <= row < max_y and 0 <= column < max_x and (row != y or column != x))]


def get_neighbors_in_direction(input_lines, y, x):
    max_y = len(input_lines)
    max_x = len(input_lines[0])
    neighbors = []
    directions = [(y1, x1) for x1 in range(-1, 2) for y1 in range(-1, 2) if not (x1 == 0 and y1 == 0)]

    for y1, x1 in directions:
        y2 = y1
        x2 = x1
        while 0 <= y2 + y + y1 < max_y and 0 <= x2 + x + x1 < max_x and input_lines[y2+y][x2+x] == '.':
            y2 += y1
            x2 += x1
        if 0 <= y + y2 < max_y and 0 <= x + x2 < max_x:
            neighbors.append((y+y2, x+x2))

    return neighbors


def model_seats(input_lines, get_neighbors, occupied_limit):
    max_y = len(input_lines)
    max_x = len(input_lines[0])

    occupied = 0
    old_occupied = -1
    while old_occupied != occupied:
        new_seats = [['.']*max_x for y in range(max_y)]
        changes = 0
        old_occupied = occupied
        occupied = 0
        for row in range(len(input_lines)):
            for column in range(len(input_lines[row])):
                neighbors = get_neighbors(input_lines, row, column)
                current_seat = input_lines[row][column]
                if current_seat == 'L' and all(input_lines[y][x] != '#' for y, x in neighbors):
                    new_seats[row][column] = '#'
                    changes += 1
                    occupied += 1
                elif current_seat == '#' and len([(y, x) for y, x in neighbors if input_lines[y][x] == '#']) >= occupied_limit:
                    new_seats[row][column] = 'L'
                    changes += 1
                else:
                    new_seats[row][column] = current_seat
                    if current_seat == '#':
                        occupied += 1

        input_lines = new_seats
    return occupied


def part_one(input_lines):
    print(model_seats(input_lines, get_neighbors_adjacent, 4))


def part_two(input_lines):
    print(model_seats(input_lines, get_neighbors_in_direction, 5))


input_lines = read_input()
part_one(input_lines)
part_two(input_lines)
