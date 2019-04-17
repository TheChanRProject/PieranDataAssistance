import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

def output(x):
    return 1.8*x + 32

X = np.arange(0,101, 0.25)
Y = output(X)

data_dict = {'x': X, 'y': Y}
df = pd.DataFrame.from_dict(data_dict)
df.head()

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.20, random_state=42)

reg = LinearRegression()
reg.fit(X_train.reshape(-1,1), Y_train.reshape(-1,1))
 Y_pred = reg.predict(X_test.reshape(-1,1))

# New Data Frame

data_dict2 = {'X_test': X_test.reshape(-1), 'Y_Predictions': Y_pred.reshape(-1), 'Y_test': Y_test.reshape(-1)}
regFrame = pd.DataFrame.from_dict(data_dict2)
regFrame.head()

# Visualize
plt.figure(figsize=(12,8))
plt.scatter(regFrame['X_test'], regFrame['Y_test'], color='green')
plt.plot(regFrame['X_test'], regFrame['Y_Predictions'], 'r-')
plt.title("Regression Plot", size=30)
plt.xlabel("X Labels", size=15)
plt.ylabel("Y Labels", size=15)

# r2 score Assessment

r_squared = r2_score(regFrame['Y_Predictions'], regFrame['Y_test'])
from IPython.display import display, Markdown
display(Markdown(f"$r^2$ = {r_squared}"))

# Mean Squared Error Assessment
mse = mean_squared_error(regFrame['Y_Predictions'], regFrame['Y_test'])
display(Markdown("$\\frac{1}{n}\\sum_{i=1}^{n}(y - \hat{y})^2$ =" + "{}".format(mse)))
