import yfinance as yf
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('fivethirtyeight')

# Create the variables and importing the data
end = datetime.now()
start = datetime(end.year-15, end.month, end.day)
stock = 'BTC-USD'
stock_data = yf.download(stock, start=start, end=end)


#Close price data handling
close_prices = stock_data['Close']

# Plot Closing price with encasement
plt.figure(figsize=(15, 6))
plt.plot(close_prices.index, close_prices, label='Close Price', color='Blue', linewidth=1)
plt.title('Close Price of Bitcoin over time', fontsize=16)
plt.xlabel('Years', fontsize=14)
plt.ylabel('Close Price', fontsize=14)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
#plt.show()