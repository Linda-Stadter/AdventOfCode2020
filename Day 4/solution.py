import re
input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines.append("\n")
        input_lines = [x.strip() for x in input_lines]
    return input_lines


def check_passport_validity(patterns):
    valid = 0
    passport = []
    input_lines = read_input()

    for line in input_lines:
        if line != "":
            passport.append(line)
        else:
            passport_str = " ".join(passport)
            passport = []
            found = 0
            for pattern in patterns:
                if re.search(pattern, passport_str):
                    found += 1
            if found == 7:
                valid += 1
    return valid


def part_one():
    birth = "byr:."
    issue = "iyr:."
    expiration = "eyr:."
    height = "hgt:."
    hair = "hcl:."
    eye = "ecl:."
    pid = "pid:."
    patterns = [birth, issue, expiration, height, hair, eye, pid]

    print(check_passport_validity(patterns))


def part_two():
    birth = "byr:((19[2-9][0-9])|(200[0-2]))($|\s)"
    issue = "iyr:((201[0-9])|(2020))($|\s)"
    expiration = "eyr:((202[0-9])|(2030))($|\s)"
    height = "hgt:((1[5-8][0-9]cm)|(19[0-3]cm)|(59in)|(6[0-9]in)|(7[0-6]in))($|\s)"
    hair = "hcl:#[0-9a-f]{6}($|\s)"
    eye = "ecl:(amb|blu|brn|gry|grn|hzl|oth)($|\s)"
    pid = "pid:[0-9]{9}($|\s)"
    patterns = [birth, issue, expiration, height, hair, eye, pid]

    print(check_passport_validity(patterns))


part_one()
part_two()
