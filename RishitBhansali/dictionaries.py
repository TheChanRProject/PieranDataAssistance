mydict = {'k1':[i for i in range(2,8)], 'k2': [(1,3), (4,5)]}

print(list(mydict.values()))
a,b = list(mydict.values())
print(a)
print(b)

for i in a:
    print(i)

for i in b:
    print(b)
