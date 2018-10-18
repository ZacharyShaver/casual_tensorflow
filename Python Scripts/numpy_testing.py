import numpy as np 

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])

'''
col 0 * 1 + col 1 * 2 + 3
1 1      1 + 2 + 3 =  
1 2
2 2 
2 3
'''
y = np.dot(X, np.array([1, 2])) + 3

print(X)
print(y)