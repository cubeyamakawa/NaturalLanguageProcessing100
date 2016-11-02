import re

with open('data/jawiki-uk.txt', 'r') as f:
    for line in f.readlines():
        data = re.search("Category:(.*)\]{2}", line)
        if data is not None:
            print(data.group(1))
