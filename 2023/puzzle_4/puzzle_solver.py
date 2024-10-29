import re
from collections import defaultdict

file_path = 'puzzle_input.txt'

def read_scratchcards(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_scratchcard(line):
    parts = re.search(r': (.+) \| (.+)', line.strip())#splitting numbers
    winning_numbers = set(map(int, parts.group(1).split()))
    owned_numbers = list(map(int, parts.group(2).split()))
    return winning_numbers, owned_numbers

def calculate_points(winning_numbers, owned_numbers):
    matches = [num for num in owned_numbers if num in winning_numbers]
    if not matches:
        return 0
    points = 1
    for i in range(1, len(matches)):
        points *= 2
    return points

def calculate_total_cards(scratchcards):
    num_dict = defaultdict(int)
    for i in range(len(scratchcards)):
        num_dict[i] = 1
    for card_idx, (winning_numbers, owned_numbers) in enumerate(scratchcards):
        matches = sum(1 for num in owned_numbers if num in winning_numbers)
        if matches > 0:
            for j in range(1, matches + 1):
                if card_idx + j < len(scratchcards):
                    num_dict[card_idx + j] += num_dict[card_idx]
    return sum(num_dict.values())

def main(file_path):
    lines = read_scratchcards(file_path)
    scratchcards = [parse_scratchcard(line) for line in lines]

    total_points = sum(calculate_points(winning, owned) for winning, owned in scratchcards)
    total_cards = calculate_total_cards(scratchcards)
    print(total_points,total_cards)

main(file_path)
