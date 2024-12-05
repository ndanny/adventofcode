"""
Part 1

- Parse each line. Count winning cards. Add 2**winning_nums-1 to the result.

Ans: 21088
"""
from pathlib import Path

input_path = Path(__file__).parent / '../input/input.txt'

result = 0

def count_winning_numbers(raw_data: str) -> int:
    data = raw_data.rstrip('\n').split(": ")[1]
    left, right = data.split(" | ")
    left, right = left.split(" "), right.split(" ")

    winning_nums = {int(elem) for elem in left if elem.isdigit()}
    your_nums = [int(elem) for elem in right if elem.isdigit()]

    return sum([1 for num in your_nums if num in winning_nums])

with open(input_path) as file:
    for line in file:
        found = count_winning_numbers(line)
        if found > 0:
            result += (2 ** (found - 1))

print('Part 1:', result)

"""
Part 2

- Pre-process input by building a map where they key is the card number and the value consists
of the winning cards, your cards, and a counter to see how many copies have been made from this card so far.
- We have to process the input backward, so we start at card 213 and work our way back.

Ans: XXX
"""

result = 0

mapping = {}

def add_card(raw_data: str, mapping: dict) -> None:
    card_info, data = raw_data.rstrip('\n').split(": ")
    left, right = data.split(" | ")
    left, right = left.split(" "), right.split(" ")

    card_number = int(card_info.split(" ")[-1])
    winning_nums = {int(elem) for elem in left if elem.isdigit()}
    your_nums = [int(elem) for elem in right if elem.isdigit()]

    mapping[card_number] = {
        'winning': winning_nums,
        'yours': your_nums,
        'copies': 0
    }

with open(input_path) as file:
    for line in file:
        add_card(line, mapping)

card_nums = sorted(mapping.keys())

for i in range(len(card_nums) - 1, -1, -1):
    n = card_nums[i]
    match_count = sum([1 for num in mapping[n]['yours'] if num in mapping[n]['winning']])
    for i in range(match_count):
        card_copy = n + i + 1
        if card_copy not in mapping:
            break
        mapping[n]['copies'] += (1 + mapping[card_copy]['copies'])

result = sum([mapping[n]['copies'] for n in mapping])

print('Part 2:', result)
