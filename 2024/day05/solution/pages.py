"""
Part 1

Ans: 5762
"""
from pathlib import Path
from collections import defaultdict

input_path = Path(__file__).parent / '../input/input.txt'

result = 0

# key: a number; value: a list of valid page numbers
# that can come after the key.
pages_after = defaultdict(set)
pages_before = defaultdict(set)
updates = []

with open(input_path) as file:
    is_rules = True
    for line in file:
        if line == '\n':
            is_rules = False
            continue

        if is_rules:
            before, after = line.split('|')
            before = int(before)
            after = int(after)
            pages_after[before].add(after)
            pages_before[after].add(before)
        else:
            updates.append([int(num) for num in line.rstrip('\n').split(',')])

def is_correct_order(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue

            before_idx = i if i < j else j
            after_idx = i if i > j else i

            if nums[after_idx] in pages_after and nums[before_idx] in pages_after[nums[after_idx]]:
                return False
            elif nums[before_idx] in pages_before and nums[after_idx] in pages_before[nums[before_idx]]:
                return False

    return True

for nums in updates:
    if is_correct_order(nums):
        mid_idx = len(nums) // 2
        result += nums[mid_idx]

print('Part 1:', result)

"""
Part 2

- <Add notes here>

Ans: XXX
"""

result = 0
print('Part 2:', result)
