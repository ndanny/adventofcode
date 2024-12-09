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

Ans: XXX
"""
from collections import deque

id = 0
expanded = []
queue = deque([])

for i in range(len(disk_map)):
    count = int(disk_map[i])
    if i % 2 == 0:
        for _ in range(count):
            expanded.append(str(id))
        queue.append({'type': 'file', 'id': id, 'count': count})
        id += 1
    else:
        for _ in range(count):
            expanded.append('.')
        queue.append({'type': 'null', 'count': count})

data = []
while queue:
    node = queue.popleft()
    count = node['count']
    if node['type'] == 'file':
       id = node['id']
       for _ in range(count):
           data.append(id)
    else:
        ptr = len(queue) - 1
        while ptr >= 0:
            if queue[ptr]['type'] == 'file' and queue[ptr]['count'] <= count:
                break
            ptr -= 1

        if ptr < 0:
            for _ in range(count):
                data.append('.')
            continue

        to_move = queue[ptr]
        queue[ptr] = {'type': 'null', 'count': to_move['count']}

        for _ in range(to_move['count']):
            data.append(to_move['id'])
        for _ in range(count - to_move['count']):
            queue.appendleft({'type': 'null', 'count': count - to_move['count']})

print(data)

checksum = 0
for i in range(len(data)):
    if data[i] == '.':
        continue
    else:
        checksum += (data[i] * i)


print('Part 2:', checksum)
