nums = [1,2,3,4,5]
nums2 = nums[0::]*2
print(nums2)

nums3 = []
for i in nums2:
    nums3.append(2*i)
print(nums3)


nums2 = [2*i for i in nums]


myLetters = list(input("Your message: "))
lettersCount = {i: myLetters.count(i) for i in myLetters}
print(lettersCount)
