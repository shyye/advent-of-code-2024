PATH_NAME = 'inputs/05_1-2.txt'
# PATH_NAME = 'inputs/test.txt'

RULES = []
PAGES = []

with open(PATH_NAME) as file:

    rules_and_pages = file.read().split('\n\n')

    rules = rules_and_pages[0].split('\n')
    pages = rules_and_pages[1].split('\n')
    
    # Save rules
    for r in rules:
        rule_items = r.split('|')
        RULES.append(rule_items)

    # Save pages
    for p in pages:
        page_items = p.split(',')
        PAGES.append(page_items)
        
result = 0
for page_update in PAGES:

    isCorrectOrder = True

    for rule in RULES:

        is_subset = set(rule).issubset(set(page_update))

        if is_subset:

            # Index of element that should be before
            b_index = page_update.index(rule[0])
            # Index of element that should be after
            a_index = page_update.index(rule[1])

            # Switch elements if thet are in wrong order
            if b_index > a_index:
                isCorrectOrder = False

                # b_value = page_update.pop(b_index)
                # a_value = int(page_update.pop(a_index))
                # page_update.insert(a_value, b_index)

                a_value = page_update.pop(a_index)
                page_update.insert(b_index, a_value)

                # page_update.remove(rule[1])
                # page_update.insert(b_index, rule[1])

                # page_update[b_index], page_update[a_index] = page_update[a_index], page_update[b_index]
        
    # Calculate mid value of originally corrected ordered pages
    if not isCorrectOrder:
        middle_index = len(page_update) // 2
        middle_number = int(page_update[middle_index])

        result += middle_number

print(result)

# One hour challenge:
#   Attempt 1 fail
#       Time left: ??