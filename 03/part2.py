import re

PATH_NAME = 'inputs/03_1-2.txt'
# PATH_NAME = 'inputs/test.txt'

MUL_PATTERN = r"mul\(\d+,\d+\)"
PATTERN_BETWEEN_DONT_AND_DO = r"(?:don't\(\).*?do\(\))"

# Everything between 'don't()' and 'do()' or 'don't()' and end of string
PATTERN_BETWEEN_DONT_AND_DO_AND_END_OF_LINE = r"(?:don't\(\).*?do\(\)|don't\(\).*?$)"  

REGEX_PATTERN_numbers = r"\d+"


result = 0
with open(PATH_NAME) as file:

    # Concatenate to one string and remove newline character to avoid missing regex matches
    data_string = ''
    for line in file:
        data_string += line.strip()

    # Remove every sequence that is betwwen don't() and do()
    cleaned_string = re.sub(PATTERN_BETWEEN_DONT_AND_DO_AND_END_OF_LINE, "", data_string)

    matches = re.findall(MUL_PATTERN, cleaned_string)
    for mul in matches:
        
        numbers = re.findall(REGEX_PATTERN_numbers, mul)
        result += int(numbers[0]) * int(numbers[1])

print(result)

# One hour challenge:
#   Attempt 1 fail
#   Attempt 2:
#       Time left: 29 min
