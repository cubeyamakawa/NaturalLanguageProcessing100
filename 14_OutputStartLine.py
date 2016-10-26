x = input('> ')
f = open('data/hightemp.txt', 'r')

for i in range(int(x)):
	print(f.readline())