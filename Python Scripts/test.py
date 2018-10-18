import quandl
import pandas as pd
import numpy
import math
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression


#wiki continous figures 
gl = quandl.get('WIKI/GOOGL')
print(type(gl))
gl = gl[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
print(type(gl))


# updating rodataframe with ws with new columns 
gl['HL_PCT'] = ( gl['Adj. High'] -  gl['Adj. Close']) /  gl['Adj. Close'] * 100.0
gl['PCT_change'] = (gl['Adj. Close'] - gl['Adj. Open']) / gl['Adj. Open'] * 100.0

gl = gl[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

print(gl.head())
