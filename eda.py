import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('data/stock_data.csv',header=[0,1])
close=data['Close']
close.plot(figsize=(12,6))
plt.show()
