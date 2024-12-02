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

- Criteria: we can remove at most one level from the report to make it safe.
- Use a monotonic stack approach (https://www.hellointerview.com/learn/code/stack/monotonic-stack).
"""
safe_reports = 0

with open(input_path) as file:
    for report in file:
        levels = list(map(int, report.split(' ')))

        if len(levels) < 2:
            safe_reports += 1
            continue

        # TODO: implement the code here.

print(f'Safe reports with at most one removal: {safe_reports}')
