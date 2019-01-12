def half(word):
	if len(word) % 2 == 0:
		half_index = len(word) / 2
		newStr = word[0:int(half_index)]
	else:
		newStr = "Length of string is not even."
	return newStr

print(half('ButterPutter'))
