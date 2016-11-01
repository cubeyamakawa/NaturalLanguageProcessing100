import json

uk = open("data/jawiki-uks.json","w")

with open("data/jawiki-country.json","r") as f:
    for line in f.readlines():
        json_file = json.loads(line)
        if json_file["title"] == "イギリス":
            text = json_file["text"]
            uk.write(text)