import numpy as np
import pandas as pd
nums = np.random.uniform(low=-20.0, high=35.0, size=(150,))
tempDict = {'celsius': [round(i,2) for i in nums]}
temp = pd.DataFrame.from_dict(tempDict)
temp.to_csv("celsius.csv")

file = open("Week2/celsius.txt", "r+")
newlines = []
for i in file.readlines():
    i = i[i.index(','):]
    i.replace(',', '')
    newlines.append(i)
lines = [i.replace(",","") for i in newlines]
sLines = "".join(lines)

file2 = open("Week2/final_celsius.txt", "x")
file2 = open("Week2/final_celsius.txt", "w")
file2.write(sLines)
file2.close()
file.close()

