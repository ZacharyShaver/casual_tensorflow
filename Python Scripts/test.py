import quandl
import pandas as pd
#wiki continous figures 
gl = quandl.get("WIKI/GOOGL")

gl = gl[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume",]]

gl["HL_PCT"] = ( gl["Adj. High"] -  gl["Adj. Close"]) /  gl["Adj. Close"] * 100.0

gl["PCT_change"] = (gl["Adj. Close"] - gl["Adj. Open"]) / gl["Adj. Open"] * 100.0



print(gl.head())