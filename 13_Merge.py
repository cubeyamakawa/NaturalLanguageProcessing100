file = open('data/13.txt', 'w')

data = [line1.replace("\n","")+"	"+line2
        for line1, line2 in zip(open('data/col1.txt'), open('data/col2.txt'))]

for i in range(len(data)):
	file.write((data[i]))
file.close()