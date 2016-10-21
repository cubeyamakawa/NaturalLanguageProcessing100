str = "パタトクカシーー"
split = list(str)
odd = ""
for i in range(1, len(split), 2):
	odd += split[i]

print(odd)
