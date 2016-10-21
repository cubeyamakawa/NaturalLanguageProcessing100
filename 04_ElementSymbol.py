import re

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = re.split('\W+', sentence)
diction = [0] * ((len(words)-1)*2)

for i in range(len(words)-1):
	word = list(words[i])
	if (i+1) == (1 or 5 or 6 or 7 or 8 or 9 or 15 or 16 or 19):
		diction[i*2] = word[0]
		diction[i*2+1] = i+1
	else:
		diction[i*2] = word[0]+word[1]
		diction[i*2+1] = i+1

diction = dict(zip(diction[0::2],diction[1::2]))
print(diction)