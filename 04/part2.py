from enum import Enum

# PATH_NAME = 'inputs/04_1-2.txt'
PATH_NAME = 'inputs/test.txt'

# Create grid from file
GRID = []
with open(PATH_NAME) as file:

    for line in file:
        character_list = list(line.strip())
        GRID.append(character_list)

GRID_LENGTH = len(GRID[0])
GRID_HEIGHT = len(GRID)


class Pointer (Enum):
    DIAGONAL_UP_LEFT = (-1, -1)
    DIAGONAL_UP_RIGHT = (1, -1)
    DIAGONAL_DOWN_LEFT = (-1, 1)
    DIAGONAL_DOWN_RIGHT = (1, 1)


WORD_TO_SEARCH = "MAS"
WORD_TO_SEARCH_REVERSED = WORD_TO_SEARCH[::-1]
WORD_LENGTH = len(WORD_TO_SEARCH)

# Current position
position = (0, 0)

# Current direction to check
direction = Pointer.DIAGONAL_UP_LEFT


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

def validate_cross(position):
    x = position[0]
    y = position[1]

    left_bound = x - 1
    right_bound = x + 1
    upper_bound = y - 1
    lower_bound = y + 1

    if (right_bound >= GRID_LENGTH or left_bound < 0 or lower_bound >= GRID_HEIGHT or upper_bound < 0):
        return False
    
    return True


def validate_new_position(x, y, direction):

    # Get values of direction to use for multiplication
    d_x = direction.value[0]
    d_y = direction.value[1]

    new_x_value = x + d_x
    new_y_value = y + d_y

    if (new_x_value >= GRID_LENGTH or new_x_value < 0 or new_y_value >= GRID_LENGTH or new_y_value < 0):
        return False
     
    return True

# Search
def search(start_position):

    word_count = 0

    is_valid_cross = validate_cross(start_position)
    if is_valid_cross:
        # \
        

    # # Get current position
    # x, y = position

    word_count = 0
    for d in directions:

        # Get current start position
        x, y = start_position

        # Store word to check against WORD_TOSEARCH
        tmp_str_1 = ""
        tmp_str_2 = ""

        # Check if it is possible to move the same number of
        # steps as the length of the WORD_TO_SEARCH
        isValidMove = validate_new_position(x, y, d)
        if isValidMove:

            x, y, _ = move(x, y, d)            
            current_letter = GRID[y][x] 

            if current_letter == 'M' or current_letter == 'S':
                if d == Pointer.DIAGONAL_UP_RIGHT or d == Pointer.DIAGONAL_UP_LEFT:
                    tmp_str_1 += current_letter
                elif d == Pointer.DIAGONAL_UP_LEFT or d == Pointer.DIAGONAL_DOWN_RIGHT:
                    tmp_str_2 == current_letter       

        
    # Duplicated code refactor BAD CODE!
    is_valid_str1 = 'M' in tmp_str_1 and 'S' in tmp_str_1
    is_valid_str2 = 'M' in tmp_str_2 and 'S' in tmp_str_2

    if is_valid_str1:
        word_count += 1

    if is_valid_str2:
        word_count += 1
                
    return word_count


result = 0
for y, row in enumerate(GRID):
    for x, letter in enumerate(row):
        if (letter == 'A'):
            
            # Update current position
            position = (x, y)

            numberOfWords = search(position)
            result += numberOfWords

print(result)