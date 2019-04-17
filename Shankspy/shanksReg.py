import pandas as pd
import seaborn as sns
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from sklearn import preprocessing
from sklearn.model_selection import cross_validate

from sklearn.linear_model import LinearRegression
url = 'https://raw.githubusercontent.com/shanksghub/FootballStats/master/FootballStats.csv'
df1 = pd.read_csv(url)
print(f"The columns are {list(df1.columns)}")
print(df1.head())


# Functional Approach for Regression Modeling
def regFunction(a,b):
    X = np.array(df1[a]).reshape(-1,1)
    Y = np.array(df1[b]).reshape(-1,1)
    
