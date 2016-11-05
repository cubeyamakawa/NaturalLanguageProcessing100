import re

dict = {}

with open('data/jawiki-uk.txt') as f:
    for line in f.readlines():
        data = re.search("\|(?P<key>.*)\s=\s(?P<object>.*)",line)

        if data is not None:
            key = data.group('key')
            object = data.group('object')

            keyTF = re.search("'{2,5}(.*)'{2,5}",data.group('key'))
            if keyTF is not None:
                key = re.sub("'{2,5}", "", data.group('key'))
            keyTF = re.search("\[\[[^ファイル](.*)\]\]", key)
            if keyTF is not None:
                key = re.sub("\[|\]", "", key)
            keyTF = re.search("{{(.*)}}", key)
            if keyTF is not None:
                key = re.sub("{{|}}", "", key)
            objectTF = re.search("'{2,5}(.*)'{2,5}",data.group('object'))
            if objectTF is not None:
                object = re.sub("'{2,5}","",data.group('object'))
            objectTF = re.search("\[\[(.*)\]\]", object)
            if objectTF is not None:
                object = re.sub("\[|\]", "", object)
            objectTF = re.search("{{(.*)}}", object)
            if objectTF is not None:
                object = re.sub("{{|}}", "", object)
            dict[key] = object
            print(object)