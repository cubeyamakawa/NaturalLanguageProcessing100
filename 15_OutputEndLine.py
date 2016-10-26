x = input('> ')
f = open('data/hightemp.txt', 'r')
num_line = sum(1 for line in open('data/hightemp.txt'))
for i in range(num_line):
	if i < num_line - int(x):	f.readline()
	else:	print(f.readline())
f.close()