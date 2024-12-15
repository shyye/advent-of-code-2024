from enum import Enum

# PATH_NAME = 'inputs/06_1-2.txt'
PATH_NAME = 'inputs/test.txt'

GRID = []

# Create GRID
with open(PATH_NAME) as file:
    for line in file:
        GRID.append(list(line.strip()))

GRID_LENGTH = len(GRID[0])
GRID_HEIGHT = len(GRID)


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


# TODO: Check if I can do this with numpy instead
# Get start position
def get_start_position(grid):
    x = -1
    y = -1

    for i, row in enumerate(GRID):

        # Check if the guard is on this row
        if '^' in row:
            y = i
            x = row.index('^')
            break
  
    return (x, y)


def is_valid_position(position):
    x = position[0]
    y = position[1]
    return x > -1 and x < GRID_LENGTH and y > -1 and y < GRID_HEIGHT


def move(current_position):

    x, y = current_position
    grid_value = GRID[x, y]

    # if grid_value == '#':


guard = {
    'position': get_start_position(),
    'direction': Direction.UP
}

start_position = get_start_position(GRID)

# Move up until #
# if '#' turn right
# else keep going
# When position is outside of GRID
#   stop cpunting steps

position = start_position

