import re

def n_gram(uni, n):
	for k in range(len(uni)-n+1):
		print(uni[k:k+n])

str = "I am an NLPer"

words = re.split('\W+', str)
chara = [k for k in str if k != " "]

n_gram(words, 2)
n_gram(chara, 2)
