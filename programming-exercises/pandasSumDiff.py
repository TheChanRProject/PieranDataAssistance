import pandas as pd 

# getting the csv data and turning into a dataframe 

df = pd.read_csv('data/fake-data.csv')

# viewing first 5 rows 

df.head() 

print(df['Value1'])

print(df['Value2']) 

# using numpy to transform columns of dataframe into numpy arrays 

import numpy as np 

value1Arr = np.array(df['Value1'])
value2Arr = np.array(df['Value2'])

# creating an add function 

def add(x,y):
    return x + y

# creating a solid subtraction function 

def subtract(x,y,z):
    if z == 'y from x':
        diff = x - y
    if z == 'x from y':
        diff = y - x
    return diff 

# assigning variables to the add or subtract operations for the first two columns of dataframe 

value3AddArr = add(value1Arr, value2Arr)

value3SubArr1 = subtract(value1Arr, value2Arr, 'y from x')

value3SubArr2 = subtract(value1Arr, value2Arr, 'x from y')

# adding new columns with assigned variables to represent the operations performed on the values 

df['Value3Add'] = value3AddArr

print(df['Value3Add']) 

df['Value3Sub1'] = value3SubArr1 

print(df['Value3Sub1'])

df['Value3Sub2'] = value3SubArr2

print(df['Value3Sub2'])