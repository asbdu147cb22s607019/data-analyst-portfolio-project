import numpy as np
import pandas as pd

data=pd.read_csv('data/stock_data.csv',header=[0,1])
returns=data['Close'].pct_change().dropna()
weights=np.array([0.4,0.3,0.2,0.1])
ret=np.sum(returns.mean()*weights)*252
vol=np.sqrt(np.dot(weights.T, np.dot(returns.cov()*252, weights)))
print(ret,vol,ret/vol)
