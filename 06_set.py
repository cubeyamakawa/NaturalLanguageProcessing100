str1 = "paraparaparadise"
str2 = "paragraph"


def n_gram(uni):
	bi_gram = [""]*(len(uni)-1)
	for k in range(len(uni)-1):
		bi_gram[k] = uni[k] + uni[k+1]
		print(bi_gram[k])
	return bi_gram

X = set(n_gram(list(str1)))
Y = set(n_gram(list(str2)))

print(X.union(Y))
print(X.difference(Y))
print(X.intersection(Y))

print(X.issuperset(['se']))
print(Y.issuperset(['se']))

