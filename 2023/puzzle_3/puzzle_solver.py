import re
from operator import mul

with open('puzzle_input.txt', 'r') as f:
    puzzle_input = f.read()


def get_parts_num_sum(puzzle_input):

    lines = puzzle_input.split('\n')

    symbol_regex = r'[^.\d]' #match any character that is not '.' or digit
    neighbor = set() #using set so we dont check for duplicates
    for i, line in enumerate(lines):
        for match in re.finditer(symbol_regex, line):
            j = match.start()
            neighbor |= {(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2)}

    number_regex = r'\d+'#match one or more digit
    part_num_sum = 0
    for i, line in enumerate(lines):
        for match in re.finditer(number_regex, line):
            if any((i, j) in neighbor for j in range(*match.span())):
                part_num_sum += int(match.group())

    return part_num_sum


def get_all_gear_ratio_sum(puzzle_input):
    lines = puzzle_input.split('\n')

    gear_regex = r'\*' #match '*'
    gears = dict()
    for i, line in enumerate(lines):
        for match in re.finditer(gear_regex, line):
            gears[(i, match.start())] = []

    number_regex = r'\d+'
    for i, line in enumerate(lines):
        for match in re.finditer(number_regex, line):
            for row in range(i-1, i+2):
                for col in range(match.start()-1, match.end()+1):
                    if (row, col) in gears:
                        gears[(row, col)].append(int(match.group()))

    gear_ratio_sum = 0
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += mul(*nums)
    return gear_ratio_sum

print(get_parts_num_sum(puzzle_input),get_all_gear_ratio_sum(puzzle_input))