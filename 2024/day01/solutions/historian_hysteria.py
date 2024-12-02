"""
Part 1

- Read input
    - Every row contains 2 integers, separated by 3 spaces.
    - Parse both integers, append the left int to list1 and right int to list2.
- Sort list1 and list2.
- Run a for-loop and take the abs diff between list1[i] and list2[i], add that to
a resulting integer.
"""
from pathlib import Path

total_distance = 0
list1, list2 = [], []

input_path = Path(__file__).parent / '../input/input.txt'

with open(input_path) as file:
    for line in file:
        row = line.strip()
        left, right = row.split('   ')
        list1.append(int(left))
        list2.append(int(right))

list1.sort()
list2.sort()

for left, right in zip(list1, list2):
    total_distance += abs(left - right)

print(total_distance)

"""
Part 2

- Build a counts dict for the elems in list2.
- Iterate over list1 and multiply list1[i] * counts[list1[i]].
    - If list1[i] not in counts, skip.
- Return the tallied "similarity score"
"""
from collections import defaultdict

similarity_score = 0

counts = defaultdict(int)
for num in list2:
    counts[num] += 1

for num in list1:
    similarity_score += (num * counts[num])

print(similarity_score)
