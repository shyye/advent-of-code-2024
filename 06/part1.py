from enum import Enum

PATH_NAME = 'inputs/06_1-2.txt'
# PATH_NAME = 'inputs/test.txt'

GRID = []

# Create GRID
with open(PATH_NAME) as file:
    for line in file:
        GRID.append(list(line.strip()))

GRID_LENGTH = len(GRID[0])
GRID_HEIGHT = len(GRID)


# class Direction(Enum):
#     UP = (0, -1)
#     RIGHT = (1, 0)
#     DOWN = (0, 1)
#     LEFT = (-1, 0)


# # Store directions in list to cycle through directions when an obstacle is met
# # TODO: Unnessessary use of enum
# directions = list(Direction)

# Directions as tuples instead of enums
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

# List of directions to cycle through
directions = [UP, RIGHT, DOWN, LEFT]


# TODO: Check if I can do this with numpy instead
# Get start position
def get_start_position():
    x = -1
    y = -1

    for i, row in enumerate(GRID):

        # Check if the guard is on this row
        if '^' in row:
            y = i
            x = row.index('^')
            break
  
    return (x, y)


def change_direction(direction):
    current_direction_index = directions.index(direction)

    # Move to the next direction (right/clockwise)
    # TODO: check this
    next_index = (current_direction_index + 1) % len(directions)
    new_direction = directions[next_index]

    return new_direction


def move(position, direction):
    
    x, y = position
    d_x, d_y = direction

    # Update position
    new_x = x + d_x
    new_y = y + d_y

    return new_x, new_y


def is_valid_position(position):
    x = position[0]
    y = position[1]
    return x > -1 and x < GRID_LENGTH and y > -1 and y < GRID_HEIGHT


guard = {
    'position': get_start_position(),
    # 'direction': Direction.UP.value
    'direction': UP
}


# Copy array to print visited tiles
grid_copy = [row[:] for row in GRID]

visited_tiles = set()   # Distinct
visited_tiles_all = []

isGuardStillWalking = True
while (isGuardStillWalking):

    # New position
    x, y = move(guard['position'], guard['direction'])
    direction = guard['direction']

    # Validate move
    if not is_valid_position((x, y)):
        break

    # Check obstacles
    grid_value = GRID[y][x]
    if grid_value == '#':
        
        direction = change_direction(direction)
        # Reset position
        x, y = guard['position']

    # Update guard data
    guard['position'] = (x, y)
    guard['direction'] = direction

    # Store data
    visited_tiles.add((x, y))
    visited_tiles_all.append((x, y))
    grid_copy[y][x] = 'X'

# Result
print(len(visited_tiles) + 1)  # plus one for the start position
print(len(visited_tiles_all))

# for row in grid_copy:
#     print(row)


# One hour challenge:
#   Attempt 1 fail
#   Attempt 2:
#       Time left: 0 min