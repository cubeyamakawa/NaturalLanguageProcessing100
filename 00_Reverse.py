str = "stressed"
reverse = ""
split = list(str)
for i in range(len(split)):
	reverse += split[(len(split) - 1) - i]

print(reverse)