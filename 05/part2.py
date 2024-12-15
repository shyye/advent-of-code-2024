import networkx as nx

PATH_NAME = 'inputs/05_1-2.txt'
# PATH_NAME = 'inputs/test.txt'

RULES = []
PAGE_UPDATES = []

# Store data
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
        PAGE_UPDATES.append(page_items)

# Topological sort, help from chatGPT and NetworkX library
result = 0
for update in PAGE_UPDATES:

    isCorrectOrder = True

    graph_of_rules = nx.DiGraph()
    for rule in RULES:

        is_subset = set(rule).issubset(set(update))
        if is_subset:
            graph_of_rules.add_edge(rule[0], rule[1])

    # Reorder rules in tolopogical order
    reordered_graph = list(nx.topological_sort(graph_of_rules))

    # Reorder the pages in the update
    reordered_update = []
    # Add pages from the sorted graph rules
    reordered_update.extend(reordered_graph)

    # Append pages not part of the graph in their original order / ChatGPT syntax
    remaining_pages = []
    for page in update:
        if page not in reordered_graph:
            remaining_pages.append(page)
    
    reordered_update.extend(remaining_pages)

    if update != reordered_update:
        isCorrectOrder = False

    # Calculate mid value of originally corrected ordered pages
    if not isCorrectOrder:
        middle_index = len(reordered_update) // 2
        middle_number = int(reordered_update[middle_index])

        result += middle_number

print(result)

# One hour challenge:
#   Attempt 1 fail
#   Attempt 2, 3, 4 fail
#       Time left: ??
# NOTE: Not so clean code, should be better