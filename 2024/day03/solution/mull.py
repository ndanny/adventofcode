"""
Part 1

- Scan the input, look for prefixes "mul(" and try to parse the
two comma separated digits, then the closing paren ")".
- Once we find "mul(", the sequence of the next value(s) must be
<int>, a comma char, another <int>, then a closing paren. If at anytime we
come across an unexpected input, break immediately and continue searching for the next mul.
- The integers to multiply are 1-3 digit numbers.

Ans: 175615763
"""
from pathlib import Path

input_path = Path(__file__).parent / '../input/input.txt'

result = 0
min_chars = len('mul(1,1)')

def parse_block(block: str):
    ptr, tally = 0, 0
    while ptr < len(block) - min_chars:
        if block[ptr:ptr+4] == 'mul(':
            ptr += 4

            a, b = '', ''

            while block[ptr].isdigit():
                a += block[ptr]
                ptr += 1

            if block[ptr] != ',':
                continue

            ptr += 1

            while block[ptr].isdigit():
                b += block[ptr]
                ptr += 1

            if block[ptr] != ')':
                continue

            tally += (int(a) * int(b))

        ptr += 1

    return tally

with open(input_path) as file:
    for block in file:
        result += parse_block(block)

print('Part 1:', result)

"""
Part 2

- Handle conditionals do() and don't()
- Keep a flag to process the next "mul(" only if its enabled.
- Also, instead of processing a block one-by-one, process all blocks as a
whole. This avoids the case where one blocks ends with a don't, and the next blocks
assumes its a do().

Ans: 74361272
"""

result = 0
min_chars = len("mul(1,1)")

def parse_block_v2(block: str):
    tally, ptr = 0, 0
    enable_mul = True
    while ptr < len(block) - min_chars:
        if block[ptr:ptr+4] == 'do()':
            ptr += 4
            enable_mul = True
        elif block[ptr:ptr+7] == "don't()":
            ptr += 7
            enable_mul = False
        elif enable_mul and block[ptr:ptr+4] == "mul(":
            ptr += 4

            a, b = "", ""

            while block[ptr].isdigit():
                a += block[ptr]
                ptr += 1

            if block[ptr] != ',':
                continue

            ptr += 1

            while block[ptr].isdigit():
                b += block[ptr]
                ptr += 1

            if block[ptr] != ')':
                continue

            tally += (int(a) * int(b))
            ptr += 1
        else:
            ptr += 1

    return tally

with open(input_path) as file:
    big_block = "".join(file.readlines())
    result += parse_block_v2(big_block)

print('Part 2:', result)
