import re

dict = {}

with open('data/jawiki-uk.txt') as f:
    for line in f.readlines():
        data = re.search("\|(?P<key>\S*)\s=\s(?P<object>\S*)",line)
        if data is not None:
            key = re.findall("'{2,5}(.*)'{2,5}",data.group('key'))
            if key is not None:
                key = re.sub(r"'+", "", data.group('key'))

            object = re.findall("'{2,5}(.*)'{2,5}",data.group('object'))
            if object is not None:
                object = re.sub(r"'","",data.group('object'))
            dict[key] = object
print(dict)