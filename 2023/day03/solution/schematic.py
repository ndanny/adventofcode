"""
Part 1

- Treat the input as a graph. Each character period, digit, or symbol
exists as a cell (i, j) in the graph.
- Scan the matrix. If we find a symbol, look in all 8 directions and see if we can find a digit.
- Scan the adjacent digits (to find the whole number), and add it to a resulting list.
    - Once done, convert each digit of the number to a period.

Ans: 525911
"""
from pathlib import Path

input_path = Path(__file__).parent / '../input/input.txt'

schematic = []

with open(input_path) as file:
    for line in file:
        line = line.strip('\n')
        schematic.append(list(line))

result = 0

directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
    (-1, -1), # Top-left diagonal
    (-1, 1),  # Top-right diagonal
    (1, -1),  # Bottom-left diagonal
    (1, 1)    # Bottom-right diagonal
]

def handle_symbol(i, j):
    count = 0

    for x_offset, y_offset in directions:
        row, col = i + x_offset, j + y_offset
        if row < 0 or row >= len(schematic) or col < 0 or col >= len(schematic[0]):
            continue

        # Found a part number!
        if schematic[row][col].isdigit():
            left = col
            right = col

            while left >= 0 and schematic[row][left].isdigit():
                left -= 1

            while right < len(schematic[0]) and schematic[row][right].isdigit():
                right += 1

            part_number = int(''.join(schematic[row][left+1:right]))
            count += part_number

            # Remember to set the part number to '...' after collecting it
            # to prevent counting it again.
            for k in range(left + 1, right):
                schematic[row][k] = '.'

    return count

for i in range(len(schematic)):
    for j in range(len(schematic[i])):
        if schematic[i][j] == ".":
            continue
        elif not schematic[i][j].isdigit():
            result += handle_symbol(i, j)

print('Part 1:', result)
