def cipher(str):
	cipher = list(str)
	str = ""
	for i in range(len(cipher)-1):
		if cipher[i].islower():
			cipher[i] = chr(219 - ord(cipher[i]))
			str += cipher[i]
	return str

print(cipher("abcdefghijk"))
print(cipher(cipher("abcdefghijk")))