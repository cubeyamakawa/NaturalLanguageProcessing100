import re

dict = {}

with open('data/jawiki-uk.txt', 'r') as f:
    for line in f.readlines():
        data = re.search("\|(?P<key>\S*)\s=\s(?P<object>\S*)",line)
        if data is not None:
            dict[data.group('key')] = data.group('object')
    print(dict)