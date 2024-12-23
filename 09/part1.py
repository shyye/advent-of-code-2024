# PATH_NAME = 'inputs/09_1-2.txt'
PATH_NAME = 'inputs/test.txt'

DISK_MAP = []

with open(PATH_NAME) as file:

    while True:

        # Read two characters each time
        chars = file.read(2)

        # Stop if the above returns an empty string
        if not chars:
            break

        # Add pairs. If the last pair isn't a pair
        # but instead a single digit, the single digit is added as it is.
        DISK_MAP.append(chars)

blocks_string = ''
current_ID = 0
for map_pair in DISK_MAP:

    num_of_blocks = int(map_pair[0])
    num_of_free_space = 0

    if len(map_pair) == 2:
        num_of_free_space = int(map_pair[1])

    blocks = num_of_blocks * str(current_ID)
    spaces = num_of_free_space * '.'

    blocks_string += blocks + spaces

    current_ID += 1

