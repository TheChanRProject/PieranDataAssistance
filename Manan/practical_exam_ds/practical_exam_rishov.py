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
