"""
Part 1

- Detect the first and last digit in the string, concatenate them,
convert to an int, and add to a resulting counter.
"""

from pathlib import Path

input_path = Path(__file__).parent / '../input/input.txt'

result = 0

with open(input_path) as file:
    for line in file:
        left = 0
        while left < len(line):
            if line[left].isdigit():
                break
            left += 1

        right = len(line) - 1
        while right >= 0:
            if line[right].isdigit():
                break
            right -= 1

        result += int(line[left] + line[right])

print(result)

"""
Part 2

- Words like "one" count as 1.
- Build a mapping of spelled-out numbers to digits.
- After scanning the word (sliding window using find() and rfind()), we will have
our resulting two digits which we add together.
"""
result = 0

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open(input_path) as file:
    for line in file:
        left = 0
        while left < len(line):
            if line[left].isdigit():
                break
            left += 1

        right = len(line) - 1
        while right >= 0:
            if line[right].isdigit():
                break
            right -= 1

        left_num = line[left]
        right_num = line[right]

        # Practically, find() and rfind() is costly.
        for digit_str, digit in digits.items():
            l_index = line.find(digit_str)
            if l_index == -1:
                continue

            if l_index < left:
                left = l_index
                left_num = digit

            r_index = line.rfind(digit_str)
            if r_index > right:
                right = r_index
                right_num = digit

        result += int(left_num + right_num)

print(result)
