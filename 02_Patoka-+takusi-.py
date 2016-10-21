str1 = "パトカー"
str2 = "タクシー"

spl1 = list(str1)
spl2 = list(str2)

sum = ""

for i in range(len(spl1)):
	sum += spl1[i] + spl2[i]

print(sum)