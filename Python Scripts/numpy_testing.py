import numpy as np 
from sklearn.linear_model import LinearRegression
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])

'''
DOT is dot product !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
col 0 * 1 + col 1 * 2 + 3
1 1     1 + 2 + 3 = 6 
1 2     1 + 4 + 3 = 8    
2 2     2 + 4 + 3 = 9
2 3     2 + 6 + 3 = 11
MATRIX MULIPLICATION
'''
y = np.dot(X, np.array([1, 2])) + 3

reg = LinearRegression().fit(X, y)


print(reg.score(X, y))

# prints scale array for dot product that was predicted 
print(reg.coef_)
# prints the intercept from the y axix 
print(reg.intercept_)

# gets the numbers for the dot product and intercept and predicts the output for points based off of that 
print(reg.predict(np.array([[10, 5]])))
