"""
Part 1

Ans: 367
"""
from pathlib import Path

input_path = Path(__file__).parent / '../input/small_2.txt'

result = 0

matrix = []

with open(input_path) as file:
    for line in file:
        matrix.append(list(line.rstrip('\n')))

freq = {}

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != '.':
            if matrix[i][j] not in freq:
                freq[matrix[i][j]] = []
            freq[matrix[i][j]].append((i, j))

antinodes = set()

def handle(freqs: list[tuple], antinodes) -> None:
    for i in range(len(freqs)):
        base_x, base_y = freqs[i]
        for j in range(i + 1, len(freqs)):
            other_x, other_y = freqs[j]

            x_diff = base_x - other_x
            y_diff = base_y - other_y

            # Given a pair of same frequencies, up to two antinodes
            # can be created.
            new_x1, new_y1 = base_x + x_diff, base_y + y_diff
            new_x2, new_y2 = other_x - x_diff, other_y - y_diff

            if new_x1 >= 0 and new_x1 < len(matrix) and \
            new_y1 >= 0 and new_y1 < len(matrix[0]):
                antinodes.add((new_x1, new_y1))

            if new_x2 >= 0 and new_x2 < len(matrix) and \
            new_y2 >= 0 and new_y2 < len(matrix[0]):
                antinodes.add((new_x2, new_y2))

    return

for f in freq:
    handle(freq[f], antinodes)

print('Part 1:', len(antinodes))

"""
Part 2

- <Add notes here>

Ans: XXX
"""

antinodes = set()

def handle_v2(freqs: list[tuple], antinodes) -> None:
    for i in range(len(freqs)):
        base_x, base_y = freqs[i]
        for j in range(i + 1, len(freqs)):
            other_x, other_y = freqs[j]

            x_diff = base_x - other_x
            y_diff = base_y - other_y

            # Given a pair of same frequencies, up to two antinodes
            # can be created.
            new_x1, new_y1 = base_x + x_diff, base_y + y_diff
            new_x2, new_y2 = other_x - x_diff, other_y - y_diff

            if new_x1 >= 0 and new_x1 < len(matrix) and \
            new_y1 >= 0 and new_y1 < len(matrix[0]):
                antinodes.add((new_x1, new_y1))

            if new_x2 >= 0 and new_x2 < len(matrix) and \
            new_y2 >= 0 and new_y2 < len(matrix[0]):
                antinodes.add((new_x2, new_y2))

    return

# Process each frequency
for f in freq:
    handle_v2(freq[f], antinodes)

print('Part 2:', len(antinodes))
