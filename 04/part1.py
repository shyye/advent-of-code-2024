from enum import Enum

class Pointer (Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, -1)
    DIAGONAL_UP_LEFT = (-1, -1)
    DIAGONAL_UP_RIGHT = (1, -1)
    DIAGONAL_DOWN_LEFT = (-1, 1)
    DIAGONAL_DOWN_RIGHT = (1, -1)

# PATH_NAME = 'inputs/04_1-2.txt'
PATH_NAME = 'inputs/test.txt'

GRID = []
WORD_TO_SEARCH = "XMAS"

# Start position
position = (0, 0)

# Current direction to check
direction = Pointer.LEFT

# Create grid from file input
with open(PATH_NAME) as file:

    for line in file:
        character_list = list(line.strip())
        GRID.append(character_list)

# Search function
def search(start_postion):
    word_count = 1


    return word_count

result = 0
for letter in GRID:
    if(letter == 'X'):
        print(letter)
        numberOfWords = search(position)
        result += numberOfWords

print(result)