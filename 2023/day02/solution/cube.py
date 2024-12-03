"""
Part 1

- Parse input, and for each subset, check if the color count surpasses the
max thresholds defined for each color.
"""
from pathlib import Path

input_path = Path(__file__).parent / '../input/input.txt'

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

result = 0

def is_possible(data: str) -> bool:
    subsets = data.split(';')
    for subset in subsets:
        subset = subset.lstrip().rstrip('\n')
        dice = subset.split(', ')
        for pair in dice:
            count, color = pair.split(' ')
            count = int(count)
            if color == 'red' and count > MAX_RED:
                return False
            elif color == 'green' and count > MAX_GREEN:
                return False
            elif color == 'blue' and count > MAX_BLUE:
                return False
    return True

with open(input_path) as file:
    for line in file:
        game, data = line.split(':')
        game_id = int(game.split(' ')[1])
        if is_possible(data):
            result += game_id

print('Part 1:', result)

"""
Part 2

- Similar to above, with some math and statefulness.
"""
result = 0

def get_cube_power(data: str) -> int:
    minimums = {'red': 0, 'green': 0, 'blue': 0}
    subsets = data.split(';')
    for subset in subsets:
        subset = subset.lstrip().rstrip('\n')
        dice = subset.split(', ')
        for pair in dice:
            count, color = pair.split(' ')
            count = int(count)
            minimums[color] = max(minimums[color], count)
    return minimums['red'] * minimums['green'] * minimums['blue']

with open(input_path) as file:
    for line in file:
        game, data = line.split(':')
        game_id = int(game.split(' ')[1])
        power = get_cube_power(data)
        result += power

print('Part 2:', result)
