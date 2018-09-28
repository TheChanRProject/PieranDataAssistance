from mean import mean

def stdv(x):
    avg = mean(x)
    sqDif = [pow(i-avg, 2) for i in x]
    return pow(sum(sqDif) / len(x), 0.5)

print(stdv([1,2,3,4,5]))
