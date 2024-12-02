file = open("./inputs/02_part1.txt")

numberOfSafeReports = 0

for line in file:
    levels = line.split()

    current_index = 0
    last_index = len(levels) - 1

    # Check if the list should be decreasing or increasing
    isDecreasingLevels = levels[0] > levels[1]
    isIncreasingLevels = levels[0] < levels[1]
    
    tempCounter = 0
    while (current_index < last_index):
        current_level = int(levels[current_index])
        next_level = int(levels[current_index + 1])

        if (abs(current_level - next_level) > 3):
            break

        if (current_level == next_level):
            break

        if (isDecreasingLevels):
            if (next_level > current_level):
                break
            else:
                tempCounter += 1
    
        if (isIncreasingLevels):
            if (next_level < current_level):
                break
            else:
                tempCounter += 1

        current_index += 1

    if (current_index + 1 == last_index):
        numberOfSafeReports += 1


print(numberOfSafeReports)


# def isReportSafe(list):
#     # Check if the list should be decreasing or increasing
#     isIncreasingLevels = list[0] < list[1]
#     isDecreasingLevels = list[0] > list[1]
