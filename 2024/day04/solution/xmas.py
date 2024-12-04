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

"""
Part 2

- The approach is similar to part 1. We can iterate over the matrix and find
the next 'A' character.
- Once found, test if its diagonal ends are 'M' and 'S', either forward or backward.
- If the condition is True, then increment the counter.

Ans: 1939
"""
result = 0

def count_xmas_v2(i: int, j: int, matrix: list[list[int]]) -> bool:
    def in_bounds(row, col):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return False
        return True

    # Handle the top-left and bottom-right.
    top_left = (-1, -1)
    bottom_right = (1, 1)
    chars = set()

    if in_bounds(i + top_left[0], j + top_left[1]):
        chars.add(matrix[i + top_left[0]][j + top_left[1]])
    else:
        return False

    if in_bounds(i + bottom_right[0], j + bottom_right[1]):
        chars.add(matrix[i + bottom_right[0]][j + bottom_right[1]])
    else:
        return False

    if chars != {'M', 'S'}:
        return False

    # Handle the top-right and bottom-left.
    top_right = (-1, 1)
    bottom_left = (1, -1)
    chars = set()

    if in_bounds(i + top_right[0], j + top_right[1]):
        chars.add(matrix[i + top_right[0]][j + top_right[1]])
    else:
        return False

    if in_bounds(i + bottom_left[0], j + bottom_left[1]):
        chars.add(matrix[i + bottom_left[0]][j + bottom_left[1]])
    else:
        return False

    if chars != {'M', 'S'}:
        return False

    return True

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 'A' and count_xmas_v2(i, j, matrix):
            result += 1

print('Part 2:', result)
