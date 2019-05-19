def max_num():
	n1 = int(input("Enter a number: "))
	n2 = int(input("Enter another number: "))
	n3 = int(input("Enter a final number: "))

	if n1 >= n2 and n1 >= n3: 
		maxNum = n1 
	elif n2 >= n1 and n2 >= n3:
		maxNum = n2 
	else:
		maxNum = n3

	return maxNum 

print(max_num()) 
