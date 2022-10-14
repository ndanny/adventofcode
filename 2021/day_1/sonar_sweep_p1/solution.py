# https://adventofcode.com/2021/day/1

f = open('2021/day_1/input.txt', 'r')

nums = []

for line in f.readlines():
    nums.append(int(line.strip()))

f.close()

inc = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        inc += 1

print(inc)
