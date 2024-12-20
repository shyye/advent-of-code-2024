import re

# PATH_NAME = 'inputs/08_1-2.txt'
PATH_NAME = 'inputs/test.txt'

GRID = []
with open(PATH_NAME) as file:
    for line in file:
        GRID.append(list(line.strip()))


# For each position in grid
#   Check if the current_value = a digit or a letter

# If current_value is a digit or letter
#   search diagonal down left
#   search diagonal down right
#   if the same letter/digit as curent letter is found
#   check the distance bewteen the nodes
#   create antinodes
#       IF they are on the grid
#       If it overlaps, it only counts one, uniue

# Regex check
regex_antenna = r"[a-z0-9]"

for row_index, row in enumerate(GRID):
    for column_index, current_value in enumerate(row):
        
        # If 
        if re.fullmatch(regex_antenna, current_value):
            pass



# Check numpy.diagonal


for row in GRID:
    print(row)