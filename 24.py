import re

with open('data/jawiki-uk.txt') as f:
    for line in f.readlines():
        data = re.search("(File|ファイル):(.*)(\|)",line)
        if data is not None:
            data = re.split(':|\|',data.group(2))
            print(data[0])