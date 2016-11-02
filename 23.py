import re

with open('data/jawiki-uk.txt') as f:
    for line in f.readlines():
        data = re.search("={2,}((.*))={2,}",line)
        if data is not None:
            section_name = line.replace("=","")
            print(int(line.count('=')/2-1),section_name)