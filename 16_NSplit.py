x = input('> ')
f = open('data/hightemp.txt', 'r')
num_lines = sum(1 for line in open('data/hightemp.txt'))
k = 1
while num_lines > k*int(x):
    file = open('data/16-'+str(k)+'txt', 'w')
    for i in range(int(x)):
        file.write(f.readline())
    file.close()
    k += 1