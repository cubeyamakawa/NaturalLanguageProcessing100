data = [line.split("	")  for line in open('data/hightemp.txt')]
col1 = [0]*len(data)
for i in range(len(data)):
	col1[i] = data[i][0]
col1 = set(col1)
print(col1)