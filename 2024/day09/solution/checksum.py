"""
Part 1

Ans: 6337367222422
"""
from pathlib import Path

input_path = Path(__file__).parent / '../input/input.txt'

disk_map = ""

with open(input_path) as file:
    for line in file:
        disk_map = line.rstrip('\n')
        break

def build_representation(disk_map: str) -> list[str]:
    id = 0
    expanded = []

    for i in range(len(disk_map)):
        count = int(disk_map[i])
        if i % 2 == 0:
            for _ in range(count):
                expanded.append(str(id))
            id += 1
        else:
            for _ in range(count):
                expanded.append('.')

    return expanded

def move_blocks(representation: list[str]) -> list[int]:
    no_gaps = []

    left, right = 0, len(representation) - 1
    while left <= right:
        if representation[right] == '.':
            right -= 1
            continue
        if representation[left].isdigit():
            no_gaps.append(int(representation[left]))
        elif representation[left] == '.':
            no_gaps.append(int(representation[right]))
            right -= 1

        left += 1

    return no_gaps

def calculate_checksum(blocks: list[int]) -> int:
    return sum(blocks[i] * i for i in range(len(blocks)))


representation = build_representation(disk_map)
blocks = move_blocks(representation)
checksum = calculate_checksum(blocks)

print('Part 1:', checksum)

"""
Part 2

- <Add notes here>

Ans: XXX
"""

result = 0
print('Part 2:', result)
