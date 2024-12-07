from enum import Enum

PATH_NAME = 'inputs/04_1-2.txt'
# PATH_NAME = 'inputs/test.txt'

# Create grid from file
GRID = []
with open(PATH_NAME) as file:

    for line in file:
        character_list = list(line.strip())
        GRID.append(character_list)

GRID_LENGTH = len(GRID[0])
GRID_HEIGHT = len(GRID)

WORD_TO_SEARCH = "MAS"
WORD_TO_SEARCH_REVERSED = WORD_TO_SEARCH[::-1]
WORD_LENGTH = len(WORD_TO_SEARCH)

# Current position
position = (0, 0)


def validate_cross(position):
    x, y = position

    left_bound = x - 1
    right_bound = x + 1
    top_bound = y - 1
    bottom_bound = y + 1

    if left_bound < 0 or right_bound >= GRID_LENGTH or top_bound < 0 or bottom_bound >= GRID_HEIGHT:
        return False
    
    return True


def search(start_position):

    x, y = start_position

    if validate_cross(start_position):
        # \
        upper_left_letter = GRID[y - 1][x - 1]
        lower_right_letter = GRID[y + 1][x + 1]
        first_diagonal = upper_left_letter + lower_right_letter

        # /
        upper_right_letter = GRID[y - 1][x + 1]
        lower_left_letter = GRID[y + 1][x - 1]
        second_diagonal = upper_right_letter + lower_left_letter

        # BAD CODE!
        first_contains_M_and_S = 'M' in first_diagonal and 'S' in first_diagonal
        second_contains_M_and_S = 'M' in second_diagonal and 'S' in second_diagonal

        if first_contains_M_and_S and second_contains_M_and_S:
            return 1

    return 0


result = 0
for y, row in enumerate(GRID):
    for x, letter in enumerate(row):
        if letter == 'A':

            # Update current position
            position = (x, y)

            numberOfWords = search(position)
            result += numberOfWords

print(result)

# One hour challenge:
#   Attempt 1 fail
#   Attempt 2:
#       Time left: 25 min