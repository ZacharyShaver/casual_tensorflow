from sklearn import datasets
import statsmodels.api as sm
import pandas as pd

b = datasets.load_boston()
df = pd.DataFrame(b.data, columns=b.feature_names)
target = pd.DataFrame(b.target, columns=["MEDV"])

x = df[["RM", "LSTAT"]]
y = target["MEDV"]


model = sm.OLS(y, x).fit()
predictions = model.predict(x)
print(model.summary())  