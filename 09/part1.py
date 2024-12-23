# PATH_NAME = 'inputs/09_1-2.txt'
PATH_NAME = 'inputs/test.txt'

DISK_MAP = []

with open(PATH_NAME) as file:

    while True:

        # Read two characters each time
        chars = file.read(2)

        # # Stop if the above returns an empty string
        if not chars:
            break

        # If the last char pair isn't a pair and instead contains a single character
        # Add 0 to indicate 0 spaces after
        if len(chars) == 1:
            chars += '0'

        DISK_MAP.append(chars)


# Pr
processed_list = []
current_ID = 0
for map_pair in DISK_MAP:

    num_of_blocks = int(map_pair[0])
    num_of_free_space = int(map_pair[1])

    blocks = num_of_blocks * str(current_ID)
    spaces = num_of_free_space * '.'

    processed_list.append(blocks)
    processed_list.append(spaces)

    current_ID += 1

