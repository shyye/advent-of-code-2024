import re

# PATH_NAME = 'inputs/03_1-2.txt'
PATH_NAME = 'inputs/test.txt'

# mul -  Match "mul".
# \(  -  Parentheses escaped with backslash.
# \d+ -  Match one or more digits.
# ,   -  Match comma
DONT_PATTERN = r"don't\(\)"
DO_PATTERN = r"do\(\)"
MUL_PATTERN = r"mul\(\d+,\d+\)"

REGEX_PATTERN_numbers = r"\d+"


result = 0
with open(PATH_NAME) as file:

    for line in file:
        matches = re.findall(DO_PATTERN, line)

        print(matches)

        # for mul in matches:
        #     numbers = re.findall(REGEX_PATTERN_numbers, mul)
        #     result += int(numbers[0]) * int(numbers[1])

print(result)

# One hour challenge:
#   Attempt 1 fail
#       Time left: 0 min
