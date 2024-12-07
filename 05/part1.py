# PATH_NAME = 'inputs/05_1-2.txt'
PATH_NAME = 'inputs/test.txt'

RULES = []
PAGES = []

with open(PATH_NAME) as file:

    rules_and_pages = file.read().split('\n\n')
    cleaned_pages = rules_and_pages[1].replace('\n', ',')
    
    RULES = rules_and_pages[0].split('\n')
    PAGES = cleaned_pages.split(',')

for p in pages:
    