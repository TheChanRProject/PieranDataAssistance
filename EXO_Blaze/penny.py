def nickel(l):
    return [f"${round(i, 1)}" for i in l]

print(nickel([10.33, 10.36, 10.67, 10.68, 10.65]))
