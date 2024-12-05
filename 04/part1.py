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


class Pointer (Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    DIAGONAL_UP_LEFT = (-1, -1)
    DIAGONAL_UP_RIGHT = (1, -1)
    DIAGONAL_DOWN_LEFT = (-1, 1)
    DIAGONAL_DOWN_RIGHT = (1, 1)


WORD_TO_SEARCH = "XMAS"
WORD_TO_SEARCH_REVERSED = WORD_TO_SEARCH[::-1]
WORD_LENGTH = len(WORD_TO_SEARCH)

# Current position
position = (0, 0)

# Current direction to check
direction = Pointer.RIGHT


# Move
# TODO: check if boolen return value is needed
def move(current_x, current_y, direction):
    x = current_x + direction.value[0]
    y = current_y + direction.value[1]

    if (x >= GRID_LENGTH or x < 0 or y >= GRID_LENGTH or y < 0):
        # Restore values
        x = current_x
        y = current_y
        return x, y, False
    
    # Assign new coordinate values
    # current_x = x
    # current_y = y
    # return True    
    return x, y, True    


def validate_new_position(x, y, direction):

    # Get values of direction to use for multiplication
    d_x = direction.value[0]
    d_y = direction.value[1]

    new_x_value = x + (WORD_LENGTH - 1) * d_x
    new_y_value = y + (WORD_LENGTH - 1) * d_y

    if (new_x_value >= GRID_LENGTH or new_x_value < 0 or new_y_value >= GRID_LENGTH or new_y_value < 0):
        return False
     
    return True

# Search
def search(start_position):

    word_count = 0
    
    # Start direction
    directions = [
        Pointer.RIGHT,
        Pointer.LEFT,
        Pointer.UP,
        Pointer.DOWN,
        Pointer.DIAGONAL_UP_LEFT,
        Pointer.DIAGONAL_UP_RIGHT,
        Pointer.DIAGONAL_DOWN_LEFT,
        Pointer.DIAGONAL_DOWN_RIGHT
    ]

    # # Get current position
    # x, y = position

    word_count = 0
    for d in directions:

        # Get current start position
        x, y = start_position

        # Store word to check against WORD_TOSEARCH
        tmp_str = ""

        # Check if it is possible to move the same number of
        # steps as the length of the WORD_TO_SEARCH
        isValidMove = validate_new_position(x, y, d)
        if isValidMove:
            for letter in WORD_TO_SEARCH:
                current_letter = GRID[y][x]
                tmp_str += current_letter

                x, y, _ = move(x, y, d)

            if WORD_TO_SEARCH == tmp_str or WORD_TO_SEARCH_REVERSED == tmp_str:
                word_count += 1
                
    return word_count


result = 0
for y, row in enumerate(GRID):
    for x, letter in enumerate(row):
        if (letter == 'X'):
            
            # Update current position
            position = (x, y)

            numberOfWords = search(position)
            result += numberOfWords

print(result)

# One hour challenge:
#   Attempt 1 fail
#   Attempt 2 fail
#   Attempt 3:
#       Time left: minus 3+ h