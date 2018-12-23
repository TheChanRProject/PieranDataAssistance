def evens(*args):
    return [e for e in args if e % 2 == 0]

print(evens(1,2,3,4,5,6,7,8,9,10))
