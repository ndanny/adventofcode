"""
Part 1

Ans: 1399219271639
"""
from pathlib import Path

input_path = Path(__file__).parent / '../input/input.txt'

result = 0

def is_valid(test_value: int, nums: list[int]) -> bool:
    combos = [nums[0]]

    for i in range(1, len(nums)):
        temp = []
        for c in combos:
            temp.append(nums[i] * c)
            temp.append(nums[i] + c)
        combos = temp

    for num in combos:
        if num == test_value:
            return True

    return False

with open(input_path) as file:
    for line in file:
        test_value, nums = line.split(": ")
        test_value = int(test_value)
        nums = [int(n) for n in nums.split(" ")]

        if is_valid(test_value, nums):
            result += test_value

print('Part 1:', result)

"""
Part 2

Ans: 275791737999003
"""

result = 0

def is_valid_v2(test_value: int, nums: list[int]) -> bool:
    combos = [nums[0]]

    for i in range(1, len(nums)):
        temp = []
        for c in combos:
            temp.append(nums[i] * c)
            temp.append(nums[i] + c)
            temp.append(int(str(c) + str(nums[i])))
        combos = temp

    for num in combos:
        if num == test_value:
            return True

    return False

with open(input_path) as file:
    for line in file:
        test_value, nums = line.split(": ")
        test_value = int(test_value)
        nums = [int(n) for n in nums.split(" ")]

        if is_valid_v2(test_value, nums):
            result += test_value

print('Part 2:', result)
