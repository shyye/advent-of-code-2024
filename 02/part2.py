# PATH_NAME = 'inputs/02_1-2.txt'
PATH_NAME = 'inputs/test.txt'

MIN_DIFF = 1
MAX_DIFF = 3
ERROR_TOLERATION = 1

numberOfSafeReports = 0


def isReportSafe(list):

    is_decreasing_list = int(list[0]) > int(list[1])
    is_increasing_list = int(list[0]) < int(list[1])

    current_index = 0
    last_index = len(list) - 1

    error_count = 0
    while (current_index < last_index):

        current = int(list[current_index])
        next = int(list[current_index + 1])

        # Check diff
        diff = abs(current - next)
        if (diff < MIN_DIFF or diff > MAX_DIFF):
            error_count += 1
        
        # if (diff == 0):
        #     error_count += 1

        # Check decreasing requirement
        if (is_decreasing_list):
            if (next > current):
                error_count += 1

        # Check increasing requirement
        if (is_increasing_list):
            if (next < current):
                error_count += 1

        current_index += 1

    if (error_count > 1):
        return False

    return True


with open(PATH_NAME) as file:

    for line in file:
        levels = line.split()
        if (isReportSafe(levels)):
            numberOfSafeReports += 1

print(numberOfSafeReports)
