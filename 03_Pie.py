import re

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = re.split('\W+',sentence)
pie = [0]*len(words)
for i in range(len(words)):
	pie[i] = len(words[i])
	print(pie[i])