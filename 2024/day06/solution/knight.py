"""
Part 1

- This is a graph/simulation problem.
- Convert the input into a 2D matrix.
- Build a dict to map the knight's icon (^, > ,v, <) to its respective direction (i.e. (0, 1) for >).
- Find the knight's starting position and run the simulation using a while loop.
- For each position visited by the knight, track it in a set.
- Return the count of the set at the end.

Ans: 4656
"""
from pathlib import Path

input_path = Path(__file__).parent / '../input/input.txt'

result = 0

matrix = []

with open(input_path) as file:
    for line in file:
        line = line.rstrip('\n')
        matrix.append(list(line))

start = ()
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '^':
            start = (i, j)
    print()

print(f"Running simulation on a {len(matrix)}x{len(matrix[0])} matrix starting at {start}.")

def print_matrix(matrix: list[list[str]]):
    for row in matrix:
        print(row)
    print()

def run_simulation(matrix: list[list[str]], start: tuple) -> int:
    visited = {start}
    r, c = start

    mapping = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
    }

    next_pos = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^',
    }

    def escaped(row: int, col: int):
        return row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0])

    while True:
        next_r = r + mapping[matrix[r][c]][0]
        next_c = c + mapping[matrix[r][c]][1]

        if escaped(next_r, next_c):
            return len(visited)
        elif matrix[next_r][next_c] == '#':
            matrix[r][c] = next_pos[matrix[r][c]]
        elif matrix[next_r][next_c] == '.':
            icon = matrix[r][c]
            matrix[r][c] = '.'
            matrix[next_r][next_c] = icon
            r, c = next_r, next_c

        visited.add((r, c))
        # print_matrix(matrix)

result = run_simulation(matrix, start)

print('Part 1:', result)

"""
Part 2

- <Add notes here>

Ans: XXX
"""

result = 0
print('Part 2:', result)
