import itertools

# PATH_NAME = 'inputs/07_1-2.txt'
PATH_NAME = 'inputs/test.txt'

OPERATORS = ['*', '+']

with open(PATH_NAME) as file:

    for line in file:
        
        test_value, numbers = line.strip().split(':')

        test_value = int(test_value)
        # operators = operators.strip().split(' ')
        numbers = [int(num) for num in numbers.strip().split(' ')]

        # TODO: combonatorics
        num_of_operators = len(numbers) - 1
        operator_combinations = list(itertools.product(OPERATORS, repeat=num_of_operators))

        # Calculate for each combination
        for combination in operator_combinations:
            