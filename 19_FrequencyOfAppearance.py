data = [line.split('	') for line in open('data/hightemp.txt')]
word_counts = {}

for i in range(len(data)):
	word = data[i][0]
	if word in word_counts:
		word_counts[word] += 1
	else:
		word_counts[word] = 1

for word, count in sorted(word_counts.items(), key=lambda x:x[1], reverse=True):
	print(word+str(count))