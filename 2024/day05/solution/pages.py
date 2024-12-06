"""
Part 1

- Build a mapping for the rules of numbers before and numbers after a certain element.
- Run a double-for loop across the list of nums and use the rules to determine correctness.

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

- For each incorrect update, run the reorder() function on it.
    - reorder() will construct a new list. It adds each n from nums into the list and
    propagates it back until it meets rule.
- In the end, all elems should be in their correct spot.

Ans: 4130
"""

result = 0

def reorder(nums: list[int]) -> list[int]:
    result = []
    for n in nums:
        result.append(n)
        ptr = len(result) - 1
        while ptr > 0 and result[ptr] in pages_before[result[ptr - 1]]:
            result[ptr], result[ptr - 1] = result[ptr - 1], result[ptr]
            ptr -= 1

    return result

for nums in updates:
    if not is_correct_order(nums):
        reordered = reorder(nums)
        mid_idx = len(nums) // 2
        result += reordered[mid_idx]

print('Part 2:', result)
