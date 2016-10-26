data = [line for line in open('data/hightemp.txt')]

file1 = open('data/col1.txt','w')
file2 = open('data/col2.txt','w')

for i in range(len(data)):
	w1 = list(data[i])[0]
	w2 = list(data[i])[1]
	if i == 0:
		write1 = w1
		write2 = w2
	else:
		write1 = "\n"+w1
		write2 = "\n"+w2
	file1.write(write1)
	file2.write(write2)
file1.close()
file2.close()

