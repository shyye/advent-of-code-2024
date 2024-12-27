# PATH_NAME = 'inputs/09_1-2.txt'
PATH_NAME = 'inputs/test.txt'

DISK_MAP = []
TOTAL_NUM_OF_BLOCKS = 0


with open(PATH_NAME) as file:

    current_ID = 0
    while True:
        
        # Read two characters each time
        chars = file.read(2)

        # Stop if the above returns an empty string
        if not chars:
            break

        # If the last char pair isn't a pair and instead contains a single character
        # Add 0 to indicate 0 spaces after
        if len(chars) == 1:
            chars += '0'

        # Add ID to the char mapping string
        #   <ID> <num of blocks> <num of spaces>' 
        #   Eg.: '123'
        #       ID: 1
        #       number of blocks: 2
        #       number of spaces: 3
        #   Will generate: 11...
        # ...
        chars_mapping = str(current_ID) + chars

        DISK_MAP.append(chars_mapping)

        # Update iteration values
        current_ID += 1
        TOTAL_NUM_OF_BLOCKS += int(chars_mapping[1])
        

num_of_files = len(DISK_MAP)
files = ''
current_num_of_blocks = 0
file_index = 0
while current_num_of_blocks < TOTAL_NUM_OF_BLOCKS:

    disk_file = DISK_MAP[file_index]

    id = str(disk_file[0])
    block_size = int(disk_file[1])
    free_spaces = int(disk_file[2])

    # Generate blocks based on the digit from the ID and add to the files collection
    files += id * block_size

    reordered_blocks = ''
    free_spaces_left = free_spaces
    while free_spaces_left != 0:

        num_of_files_to_reorder = 0

        last_disk_file = DISK_MAP[num_of_files - 1]
        last_file_id = str(last_disk_file[0])
        num_of_blocks_left = int(last_disk_file[1])
        last_filefree_spaces = int(last_disk_file[2])

        if free_spaces_left > num_of_blocks_left:
            num_of_files_to_reorder = num_of_blocks_left
        else:
            num_of_files_to_reorder = free_spaces_left

        reordered_blocks += last_file_id * num_of_files_to_reorder

        # Update iteration values
        num_of_blocks_left -= num_of_files_to_reorder
        free_spaces_left -= num_of_files_to_reorder
        # TODO: fix structur, not overriding here
        if current_num_of_blocks >= TOTAL_NUM_OF_BLOCKS:
            free_spaces_left = 0


        # Remove check for last file if there are no blocks left
        if num_of_blocks_left == 0:
            num_of_files -= 1
        else:
            # Adjust the block_size of the last file
            DISK_MAP[num_of_files - 1] = last_file_id + str(num_of_blocks_left) + str(last_filefree_spaces)

    files += reordered_blocks

    # current_num_of_blocks += block_size + REORDED_BLOCKS
    # TOTAL_NUM_OF_BLOCKS
    file_index += 1
    current_num_of_blocks = len(files)




    






# for disk_file in DISK_MAP:

#     num_of_blocks = int(map_pair[0])
#     num_of_free_space = int(map_pair[1])

#     blocks = num_of_blocks * str(current_ID)
#     # spaces = num_of_free_space * '.'

#     # blocks = (str(current_ID), num_of_blocks)
#     # spaces = ('.', num_of_free_space)
#     spaces = num_of_free_space

#     # disk_file = (current_ID, num_of_blocks, num_of_free_space)
#     # files.append(disk_file)

#     block_list.append(blocks)
#     spaces_list.append(spaces)

#     current_ID += 1


    



# One hour challenge:
#   Attempt 1 fail
#   Attempt 2 fail
#   Attempt 3 fail overthiiink
#   Attempt 4, 5 fail?
#   Attempt 5: 
#       Time left: ???