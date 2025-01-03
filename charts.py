import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('fivethirtyeight')

# Create the variables and importing the data
end = datetime.now()
start = datetime(end.year-15, end.month, end.day)
stock = 'BTC-USD'
stock_data = yf.download(stock, start=start, end=end)

# Calculate Moving Averages
stock_data['MA_365'] = stock_data['Close'].rolling(window=365).mean()
stock_data['MA_100'] = stock_data['Close'].rolling(window=100).mean()

# Plot Closing price with Moving Averages
plt.figure(figsize=(15, 6))
plt.plot(stock_data.index, stock_data['Close'], label='Close Price', color='Blue', linewidth=2)
plt.plot(stock_data.index, stock_data['MA_365'], label='365-Day MA', color='Red', linestyle = '--', linewidth=2)
plt.plot(stock_data.index, stock_data['MA_100'], label='100-Day MA', color='Green', linestyle = '--', linewidth=2)
plt.title('Close Price of Bitcoin with Moving Averages', fontsize=16)
plt.xlabel('Years', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show() 