# https://adventofcode.com/2021/day/1#part2

f = open('2021/day_1/input.txt', 'r')

nums = []

for line in f.readlines():
    nums.append(int(line.strip()))

f.close()

inc = 0
window_size = 3

for i in range(3, len(nums)):
    # Optimization: cache the current window and use it as the previous window
    curr_window = sum(nums[i - window_size:i])
    prev_window = sum(nums[i - 1 - window_size:i-1])

    if curr_window > prev_window:
        inc += 1

print(inc)
