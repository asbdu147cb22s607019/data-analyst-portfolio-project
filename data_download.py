import yfinance as yf
import pandas as pd

stocks=["AAPL","TSLA","MSFT","AMZN"]
data=yf.download(stocks,start="2018-01-01",end="2024-12-31")
data.to_csv("data/stock_data.csv")
print("Data downloaded!")
