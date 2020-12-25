import re
from collections import defaultdict
from constraint import *
input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines = [x.strip() for x in input_lines]

    return input_lines


def get_fields(input_lines):
    fields = {}
    for line in input_lines:
        match = re.match("(.*): ([\d-]+) or ([\d-]+)", line)
        match = match.groups()
        valid = []
        valid.append(match[1].split('-'))
        valid.append(match[2].split('-'))
        fields[match[0]] = valid
    return fields


def part_one(input_lines):
    fields = get_fields(input_lines[:20])
    invalid_numbers = []
    invalid_tickets = set()

    for ticket in input_lines[25:]:
        for num in ticket.split(','):
            is_valid = False
            for key in fields:
                values = fields[key]
                for values in fields[key]:
                    if int(values[0]) <= int(num) <= int(values[1]):
                        is_valid = True

            if not is_valid:
                invalid_numbers.append(int(num))
                invalid_tickets.add(ticket)

    print(sum(invalid_numbers))
    return list(set(input_lines[25:]) - invalid_tickets)


def part_two(input_lines, valid_tickets):
    fields = get_fields(input_lines[:20])
    solution = defaultdict(list)

    for key in fields:
        for i in range(len(fields)):
            is_valid = True
            for ticket in valid_tickets:
                ticket = ticket.split(',')

                if not (int(fields[key][0][0]) <= int(ticket[i]) <= int(fields[key][0][1]) or
                        int(fields[key][1][0]) <= int(ticket[i]) <= int(fields[key][1][1])):
                    is_valid = False
                if not is_valid:
                    break

            if is_valid:
                solution[key].append(i)
            else:
                continue

    problem = Problem()
    for k, v in solution.items():
        problem.addVariable(k, v)
    problem.addConstraint(AllDifferentConstraint())
    solution = problem.getSolutions()[0]

    my_ticket = input_lines[22].split(',')
    answer = 1
    for field in ['departure location', 'departure station', 'departure platform',
                  'departure track', 'departure date', 'departure time']:
        answer *= int(my_ticket[solution[field]])

    print(answer)


input_lines = read_input()
valid_tickets = part_one(input_lines)
part_two(input_lines, valid_tickets)
