def maxNum():
	n1 = int(input("Put in a number: "))
	n2 = int(input("Put in another number: ")) 
	n3 = int(input("Put in a final number: ")) 

	nums = [n1, n2, n3] 

	return max(nums) 

print(maxNum()) 
