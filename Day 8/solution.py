import re
input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines = [x.strip() for x in input_lines]

    return input_lines


def part_one(input_lines):
    accumulator, finished = run_instructions(input_lines)
    print(accumulator)


def run_instructions(input_lines):
    pattern_nop = "nop ([+-]?\d+)"
    pattern_acc = "acc ([+-]?\d+)"
    pattern_jmp = "jmp ([+-]?\d+)"

    i = 0
    visited = []
    accumulator = 0
    while i < len(input_lines):
        if i in visited:
            return (accumulator, False)

        visited.append(i)
        nop = re.findall(pattern_nop, input_lines[i])
        acc = re.findall(pattern_acc, input_lines[i])
        jmp = re.findall(pattern_jmp, input_lines[i])

        if nop:
            i += 1
            continue
        elif acc:
            i += 1
            accumulator += int(acc[0])
            continue
        elif jmp:
            i += int(jmp[0])

    return (accumulator, True)


def part_two(input_lines):
    pattern_nop = "nop ([+-]?\d+)"
    pattern_acc = "acc ([+-]?\d+)"
    pattern_jmp = "jmp ([+-]?\d+)"

    for i in range(len(input_lines)):
        nop = re.findall(pattern_nop, input_lines[i])
        jmp = re.findall(pattern_jmp, input_lines[i])
        acc = re.findall(pattern_acc, input_lines[i])

        if acc:
            continue
        elif nop:
            new_line = "jmp {}".format(nop[0])
        elif jmp:
            new_line = "nop {}".format(jmp[0])

        input_tmp = input_lines[:]
        input_tmp[i] = new_line
        accumulator, finished = run_instructions(input_tmp)

        if finished:
            print(accumulator)


input_lines = read_input()
part_one(input_lines)
part_two(input_lines)
