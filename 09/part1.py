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
for char_pair in DISK_MAP:

    if len(char_pair) == 1:

# One hour challenge:
#   Attempt 1 fail
#   Attempt 2:
#       Time left: ???