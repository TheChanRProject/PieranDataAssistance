import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from IPython.display import display, Markdown 

from sklearn.linear_model import LinearRegression
url = 'https://raw.githubusercontent.com/shanksghub/FootballStats/master/FootballStats.csv'
df1 = pd.read_csv(url)
print(f"The columns are {list(df1.columns)}")
print(df1.head())


# Functional Approach for Regression Modeling
def regFunction(df, a,b, position):
    X = np.array(df[a]).reshape(-1,1)
    Y = np.array(df[b]).reshape(-1,1)
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)
    reg = LinearRegression()
    reg.fit(X_train, Y_train)
    Y_pred = reg.predict(X_test)
    r_square = r2_score(Y_pred, Y_test)
    mse = mean_squared_error(Y_pred, Y_test)
    display(Markdown(f"$ r^2 value = {r_square*100}% $"))
    display(Markdown("$\\frac{1}{n}\\sum_{i=1}^{n}(\hat{y} - y)^2$" + f"= {mse}"))
    # visualization
    plt.figure(figsize=(12,8))
    plt.scatter(X_test, Y_test)
    plt.plot(X_test, Y_pred)
    plt.title(f"Regression between {a} and {b}", size=30)
    plt.xlabel(a, size=15)
    plt.ylabel(b, size=15)
    plt.show()
    plt.savefig(f"images/reg_{a}_{b}_{position}.png")
    # Reg Frame
    reg_dict = {f'test_{a}': X_test, f'test_{b}': Y_test, f'pred_{b}': Y_pred}
    regFrame = pd.DataFrame.from_dict(reg_dict)
    return regFrame

forwardFrame = df1.loc[df1['position'] == 'Forward']
forwardFrame.head()

print(regFunction(forwardFrame, 'shots', 'goals', 'Forward'))
