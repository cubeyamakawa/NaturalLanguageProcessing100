import re

with open('data/jawiki-uk.txt', 'r') as f:
    for line in f.readlines():
        if re.search("Category", line):
            print(line)