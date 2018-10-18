from sklearn import linear_model, datasets
import pandas as pd 

#loading data into pandas dataframe 
data = datasets.load_boston()                           #boston dataset
df = pd.DataFrame(data.data, columns=data.feature_names)
target = pd.DataFrame(data.target, columns=["MEDV"])

x = df
y = target["MEDV"]

lm = linear_model.LinearRegression()
model = lm.fit(x,y)
pred = lm.predict(x)
print(pred[0:5])


