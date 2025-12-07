import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('data/stock_data.csv',header=[0,1])
returns=data['Close'].pct_change().dropna()
sns.heatmap(returns.corr(),annot=True)
plt.show()
