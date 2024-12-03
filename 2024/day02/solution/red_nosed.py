"""
Part 1

Context:
- In the input file, each line represents one report.
    - Each report contains levels, each separated by one space.
- Figure out which reports are safe.
    - All levels inc or dec.
    - Diff of each level is within [1, 3]

Approach:
- Parse input and process line-by-line.
- Iterate over the levels, use a pointer and lookback to determine eligibility.
    - Based on report[0] and report[1], we can track if the report is inc or dec.
- For each safe report, increment the counter by 1.
"""
from pathlib import Path

safe_reports = 0

input_path = Path(__file__).parent / '../input/input.txt'

def check_report(levels: list[int]) -> bool:
    """Returns True if the report is safe."""
    increasing = levels[1] > levels[0]

    for i in range(1, len(levels)):
        if increasing and levels[i] <= levels[i - 1] or \
        not increasing and levels[i] >= levels[i - 1] or \
        abs(levels[i] - levels[i - 1]) not in range(1, 4):
            return False

    return True

with open(input_path) as file:
    for report in file:
        levels = list(map(int, report.split(' ')))

        # Handle reports with < 2 levels
        if len(levels) < 2:
            safe_reports += 1
            continue

        if check_report(levels):
            safe_reports += 1

print(f'Safe reports: {safe_reports}')

"""
Part 2

- Bruteforce approach.
- Check the report after attempting to remove every level.
- At the end, if no combo works, then don't count that report.
"""

safe_reports = 0

def check_report_brute(levels):
    if check_report(levels):
        return True

    for i in range(len(levels)):
        # Remove levels[i] and check the report.
        if check_report(levels[:i] + levels[i+1:]):
            return True

    return False

with open(input_path) as file:
    for report in file:
        levels = list(map(int, report.split(' ')))

        if len(levels) < 2:
            safe_reports += 1
            continue

        if check_report_brute(levels):
            safe_reports += 1

print(f'Safe reports with at most one removal (bruteforce): {safe_reports}')


"""
Part 2 (monotonic stack) - Unfinished

- More optimal than the brute-force for large report sizes.
- Criteria: we can remove at most one level from the report to make it safe.
- Use a monotonic stack approach (https://www.hellointerview.com/learn/code/stack/monotonic-stack).
"""
safe_reports = 0

def next_greater(levels: list[int]):
    # Calculate x-indices away until we see the next inc number.
    n = len(levels)
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and levels[i] > levels[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result

def next_smaller(levels: list[int]):
    # Calculate x-indices away until we see the next dec number.
    n = len(levels)
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and levels[i] < levels[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result

def is_valid(levels: list[int], monotonic: list[int]) -> bool:
    """Given the levels input and the monotonic result, determine if the report
    meets the criteria for being safe with at most one penalty.
    """
    # We can only afford 1 penalty at most.
    # Track the bad index.
    penalty, bad_idx = 0, None

    # Calculate the count of non-1s.
    # if monotonic[i] != 1, then the next increasing or decreasing value is not
    # 1-away and we can penalize.
    for i in range(len(monotonic) - 1):
        if monotonic[i] != 1:
            penalty += 1
            bad_idx = i
            if penalty > 1:
                return False

    levels_copy = levels[:]
    if bad_idx is not None:
        del levels_copy[bad_idx]

    # Sanity check the range of each adjacent diff.
    for i in range(1, len(levels_copy)):
        adjacent_diff = abs(levels_copy[i] - levels_copy[i - 1])
        if adjacent_diff not in range(0, 4):
            penalty += 1
            if penalty > 1:
                return False

    return True

def check_report_v2(levels: list[int]) -> bool:
    # Calculate x-indices way until we see the next inc/dec number.
    inc = next_greater(levels)
    dec = next_smaller(levels)
    return is_valid(levels, inc) or is_valid(levels, dec)

with open(input_path) as file:
    for report in file:
        levels = list(map(int, report.split(' ')))

        if len(levels) < 2:
            safe_reports += 1
            continue

        if check_report_v2(levels):
            safe_reports += 1

print(f'Safe reports with at most one removal (monotonic stack): {safe_reports}')
