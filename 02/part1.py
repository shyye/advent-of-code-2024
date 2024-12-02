PATH_NAME = 'inputs/02_1.txt'
# PATH_NAME = 'inputs/test.txt'

MIN_DIFF = 1
MAX_DIFF = 3

numberOfSafeReports = 0


def isReportSafe(list):

    is_decreasing_list = int(list[0]) > int(list[1])
    is_increasing_list = int(list[0]) < int(list[1])

    current_index = 0
    last_index = len(list) - 1

    while (current_index < last_index):

        current = int(list[current_index])
        next = int(list[current_index + 1])

        # Check diff
        diff = abs(current - next)
        if (diff < MIN_DIFF or diff > MAX_DIFF):
            return False

        # Check decreasing requirement
        if (is_decreasing_list):
            if (next > current):
                return False

        # Check increasing requirement
        if (is_increasing_list):
            if (next < current):
                return False

        current_index += 1

    return True


with open(PATH_NAME) as file:

    for line in file:
        levels = line.split()
        if (isReportSafe(levels)):
            numberOfSafeReports += 1

print(numberOfSafeReports)

# One hour challenge:
#   Attempt 1 fail
#   Attempt 2:
#       Time left: 12:00
