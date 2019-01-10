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
