import re
from collections import defaultdict
input_path = "input.txt"
found = defaultdict(list)


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines = [x.strip() for x in input_lines]

    return input_lines


def define_rules(input_lines):
    rules = defaultdict(list)
    for line in input_lines:
        outer_bag = re.findall("(^.+) bags contain", line)
        inner_bags = re.findall("(\d) ([a-z]+ [a-z]+) bag", line)
        rules[outer_bag[0]] = [a for i, x in inner_bags for a in [x]*int(i)]

    return rules


def part_one(rules):
    bag_counter = 0
    search_list = ["shiny gold"]
    i = 0

    while i < len(search_list):
        for k, v in rules.items():
            if search_list[i] in v and k not in search_list:
                bag_counter += 1
                search_list.append(k)
        i += 1

    print(bag_counter)


def get_containing_bags(bag, rules):
    if len(found[bag]) > 0:
        return found[bag]

    res = []
    for b in rules[bag]:
        res.append(b)
        res.extend(get_containing_bags(b, rules))
    found[bag] = res

    return res


def part_two(rules):
    print(len(get_containing_bags("shiny gold", rules)))


input_lines = read_input()
rules = define_rules(input_lines)
part_one(rules)
part_two(rules)
