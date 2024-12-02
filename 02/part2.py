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
            
            # If next index is the last index, the report can be safe if this error is removed.
            isLastIndex = (current_index + 1) == last_index
            if (isLastIndex):
                print("hej")
                error_count += 1
            else:
                # [current, next, nextNext] Check current and next-next value
                current_index += 1
                current = int(list[current_index])
                next = int(list[current_index + 1])

                nextDiff = abs(current - next)
                if (nextDiff < MIN_DIFF or nextDiff > MAX_DIFF):
                    return False
                else:
                    error_count += 1

        # Check decreasing requirement
        if (is_decreasing_list):
            if (next > current):
                error_count += 1

            # Check increasing requirement
        if (is_increasing_list):
            if (next < current):
                error_count += 1
            
        current_index += 1
    
    if (error_count > ERROR_TOLERATION):
        return False

    return True


with open(PATH_NAME) as file:

    for line in file:
        levels = line.split()
        if (isReportSafe(levels)):
            numberOfSafeReports += 1

        print(isReportSafe(levels))

print(numberOfSafeReports)

# One hour challenge:
#   Attempt 1 fail
#   Attempt 2 fail
#       Time left: ??
