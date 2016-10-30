file = [line.split('	') for line in open('data/hightemp.txt')]
file.sort(key=lambda x:x[2], reverse=True)

for i in range(len(file)):
	print(file[i])