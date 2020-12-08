input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines.append("\n")
        input_lines = [x.strip() for x in input_lines]
    return input_lines


def part_one():
    input_lines = read_input()
    group_counts = []
    yes_answers = set()

    for line in input_lines:
        if not line:
            group_counts.append(len(yes_answers))
            yes_answers = set()
        else:
            for c in line:
                yes_answers.add(c)

    print(sum(group_counts))


def part_two():
    input_lines = read_input()
    group_counts = []
    yes_answers = []

    for line in input_lines:
        if not line:
            answer_intersection = yes_answers[0]
            for answer_set in yes_answers:
                answer_intersection = answer_intersection.intersection(answer_set)
            group_counts.append(len(answer_intersection))
            yes_answers = []
        else:
            yes_answers.append(set(line))

    print(sum(group_counts))


part_one()
part_two()
