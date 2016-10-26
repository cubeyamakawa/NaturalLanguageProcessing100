import random

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = str.split(" ")

for i in range(len(words)-1):
	chara = list(words[i])
	if len(words[i]) > 5:
		for k in range(1,len(chara)-1):
			chara[1:-1] = random.sample(chara[1:-1], len(chara)-2)
	words[i] = "".join(chara)

print(" ".join(words))