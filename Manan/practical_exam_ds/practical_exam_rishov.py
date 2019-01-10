import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf

# Problem 1

boston_df = pd.read_csv("Manan/practical_exam_ds/data/housing.csv")
boston_df.head()

sns.set(rc={'figure.figsize':(10.5,5.5)})
ax = sns.distplot(boston_df['MEDV'], bins=30)
ax.set_title("Distribution of Boston House Prices")
ax.set_xlabel("Price in Thousands ($)")
ax.set_ylabel("Frequency")
ax.plot()

# Measuring Linear Relationships Between the Variables

# Correlation Matrix

correlation_matrix = boston_df.corr().round(2)

# Visualization using seaborn heatmap

sns.heatmap(data=correlation_matrix, annot=True).set_title("Correlation Matrix")

# Scatterplots of features with target

plt.figure(figsize=(10,3))

features = ['LSTAT', 'RM']
target = boston_df['MEDV']

for i,col in enumerate(features):
    plt.subplot(1, len(features),i+1)
    x = boston_df[col]
    y = target
    plt.scatter(x,y,marker='o')
    plt.title(col)
    plt.xlabel(f"Correlation between {col} and MEDV")
    plt.ylabel('MEDV')

 # Concatenate features into one dataframe

X = pd.DataFrame(np.c_[boston_df['LSTAT'], boston_df['RM']], columns = ['LSTAT','RM'])

# Setting dependent variable MEDV as Y
Y = boston_df['MEDV']

# Splitting data into training and testing sets. Training will be on 80% of the samples
# and testing on the other 20%

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=5)
print(f"Shape of X training set: {X_train.shape} \nShape of Y training set: {X_test.shape} \nShape of X test set: {Y_train.shape} \nShape of Y test set: {Y_test.shape}")
