file = open("./inputs/01_part1.txt", "r")

first_list = []
second_list = []

for line in file:
    line_items = line.split()
    first_list.append(int(line_items[0]))
    second_list.append(int(line_items[1]))

total_distance = 0
while (len(first_list) != 0 and len(second_list) != 0):

    first_min = min(first_list)
    second_min = min(second_list)

    first_list.remove(first_min)
    second_list.remove(second_min)

    total_distance += abs((first_min - second_min))

print(total_distance)

# One hour challenge:
#   Time left: 27:15
