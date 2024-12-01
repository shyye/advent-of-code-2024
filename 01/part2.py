file = open("./inputs/01_part1.txt", "r")

first_list = []
second_list = []

for line in file:
    line_items = line.split()
    first_list.append(int(line_items[0]))
    second_list.append(int(line_items[1]))

total_distance = 0
while (len(first_list) != 0 and len(second_list) != 0):

    # Current item from left list
    current_item = first_list[0]

    # Occurences in right list
    occurences_in_second_list = second_list.count(current_item)

    total_distance += current_item * occurences_in_second_list

    first_list.pop(0)

print(total_distance)

# One hour challenge:
#   Time left: 51:10
