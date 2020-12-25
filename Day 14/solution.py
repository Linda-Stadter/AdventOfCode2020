import re
import math
input_path = "input.txt"


def read_input():
    with open(input_path, "r") as input_file:
        input_lines = input_file.readlines()
        input_lines = [x.strip() for x in input_lines]

    return input_lines


def part_one(input_lines):
    mask_pattern = "mask = ([X|\d]{36})"
    mem_pattern = "mem\[(\d*)\] = (\d*)"
    mask = 0
    mem = {}

    for line in input_lines:
        findall_mask = re.findall(mask_pattern, line)
        findall_mem = re.findall(mem_pattern, line)

        if findall_mask:
            mask = findall_mask[0]
        elif findall_mem:
            num = list(str("{0:036b}".format(int(findall_mem[0][1]))))

            for i, c in enumerate(mask):
                if c != 'X':
                    num[i] = c

            mem[int(findall_mem[0][0])] = int(''.join(num), 2)

    print(sum([v for k, v in mem.items()]))


def part_two(input_lines):
    mask_pattern = "mask = ([X|\d]{36})"
    mem_pattern = "mem\[(\d*)\] = (\d*)"
    mask = 0
    mem = {}

    for line in input_lines:
        findall_mask = re.findall(mask_pattern, line)
        findall_mem = re.findall(mem_pattern, line)

        if findall_mask:
            mask = findall_mask[0]
        elif findall_mem:
            num = int(findall_mem[0][1])
            original_address = list(str("{0:036b}".format(int(findall_mem[0][0]))))
            addresses = ['']

            for i, c in enumerate(mask):
                new_addresses = []
                for address in addresses:
                    if c == '0':
                        address += original_address[i]
                        new_addresses.append(address)
                    if c == '1':
                        address += '1'
                        new_addresses.append(address)
                    if c == 'X':
                        floating = address + '0'
                        new_addresses.append(floating)
                        floating = address + '1'
                        new_addresses.append(floating)
                addresses = new_addresses[:]

            for address in addresses:
                mem[int(''.join(address), 2)] = int(findall_mem[0][1])

    print(sum([v for k, v in mem.items()]))


input_lines = read_input()
part_one(input_lines)
part_two(input_lines)
