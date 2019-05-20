def multMax(n):
    nums = []
    while len(nums) < n:
        x = float(input("Please type in a number: "))
        nums.append(x)
    print(max(nums))
    return max(nums)
