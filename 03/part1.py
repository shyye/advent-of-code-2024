import re

PATH_NAME = 'inputs/03_1.txt'
# PATH_NAME = 'inputs/test.txt'

# mul -  Match "mul".
# \(  -  Parentheses escaped with backslash.
# \d+ -  Match one or more digits.
# ,   -  Match comma
REGEX_PATTERN = r"mul\(\d+,\d+\)"
REGEX_PATTERN_numbers = r"\d+"


result = 0
with open(PATH_NAME) as file:

    for line in file:
        matches = re.findall(REGEX_PATTERN, line)

        for mul in matches:
            numbers = re.findall(REGEX_PATTERN_numbers, mul)
            result += int(numbers[0]) * int(numbers[1])

print(result)

# One hour challenge:
#   Attempt 1:
#       Time left: 5 min