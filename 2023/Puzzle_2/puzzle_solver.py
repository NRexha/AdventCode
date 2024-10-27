import re
import math

with open('puzzle_input.txt', 'r') as file:
    puzzle_input = file.read()

def possible_ids_sum(puzzle_input):
    possible = [12, 13, 14]
    ids_sum = 0
    for game_id, game in enumerate(puzzle_input.split('\n'), start=1):
        for cube_count, color in re.findall(r'(\d+) (red|green|blue)', game):
            color_index = ['red', 'green', 'blue'].index(color)
            if possible[color_index] < int(cube_count):
                break
        else:
            ids_sum += game_id

    return ids_sum

def total_power_sum(puzzle_input):
    power_sum = 0
    for game in puzzle_input.split('\n'):
        max_number = [0, 0, 0]
        for cube_count, color in re.findall(r'(\d+) (red|green|blue)', game):
            color_index = ['red', 'green', 'blue'].index(color) 
            max_number[color_index] = max(int(cube_count), max_number[color_index]) 

        power_sum += math.prod(max_number)

    return power_sum

print(possible_ids_sum(puzzle_input),total_power_sum(puzzle_input))
