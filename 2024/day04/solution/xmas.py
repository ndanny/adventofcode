"""
Part 1

- Read input file and build the mxn matrix (each cell is a letter).
- Iterate over the matrix, when an instance of 'x' is found, scan all 8 directions
to find the word 'xmas'. If one is found, then add that to a count var.

Ans: 2547
"""
from pathlib import Path

input_path = Path(__file__).parent / '../input/input.txt'

matrix = []

# Read file and build matrix
with open(input_path) as file:
    for line in file:
        matrix.append(line)

result = 0
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def count_xmas(i: int, j: int, matrix: list[list[str]]) -> int:
    if matrix[i][j] != 'X':
        return 0

    # x is already found, so we look for m, a, and s.
    found = 0
    for x, y in directions:
        m, a, s = False, False, False

        # (i, j) needs to stretch in at least 3 more cells.
        max_row = i + (3 * x)
        max_col = j + (3 * y)
        if max_row < 0 or max_row >= len(matrix) or max_col < 0 or max_col >= len(matrix[0]):
            continue

        if matrix[i + x][j + y] == 'M':
            m = True
        if matrix[i + (2 * x)][j + (2 * y)] == 'A':
            a = True
        if matrix[i + (3 * x)][j + (3 * y)] == 'S':
            s = True

        if m and a and s:
            found += 1

    return found

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 'X':
            result += count_xmas(i, j, matrix)

print('Part 1:', result)
