import itertools

PATH_NAME = 'inputs/07_1-2.txt'
# PATH_NAME = 'inputs/test.txt'

OPERATORS = ['*', '+', '||']

correct_values_sum = 0

with open(PATH_NAME) as file:

    for line in file:
        
        test_value, numbers = line.strip().split(':')

        test_value = int(test_value)
        numbers = [int(num) for num in numbers.strip().split(' ')]

        # Combonatorics - Cartesian Product
        # Find all combinations of operators, order matters
        num_of_operators = len(numbers) - 1
        operator_combinations = list(itertools.product(OPERATORS, repeat=num_of_operators))

        # Check all possible combination
        for combination in operator_combinations:

            # Calculate sum for this combination
            # E.g. 1 + 2 * 3
            sum = 0
            for i in range(num_of_operators):

                if i == 0:
                    number_before = numbers[i]
                else:
                    # The sum of the previous calculations
                    number_before = sum

                operator = combination[i]
                number_after = numbers[i + 1]

                if operator == '*':
                    sum = number_before * number_after
                elif operator == '+':
                    sum = number_before + number_after
                elif operator == '||':
                    num_str = str(number_before) + str(number_after)
                    sum = int(num_str)

                # Break if the sum is invalid before the whole expression has been calculated 
                if sum > test_value:
                    break
            
            if sum == test_value:
                correct_values_sum += test_value
                break

print(correct_values_sum)

# One hour challenge:
#   Attempt 1:
#       Time left: 47 min

# NOTE: This code is slow, how can I make it better and avoid nested loops?
