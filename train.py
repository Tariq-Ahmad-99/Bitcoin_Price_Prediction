import os
import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential # type: ignore
from keras.layers import Dense, LSTM # type: ignore
plt.style.use('fivethirtyeight')

# Create the variables and importing the data
end = datetime.now()
start = datetime(end.year-15, end.month, end.day)
stock = 'BTC-USD'
stock_data = yf.download(stock, start=start, end=end)

# Close price data handling
close_prices = stock_data['Close'].dropna()  # Drop any NaN values


## Building the LSTM model

# Scale the data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(close_prices.values.reshape(-1, 1))

# Prepare data for the model
x_data = []
y_data = []
base_days = 100
for i in range(base_days, len(scaled_data)):
    x_data.append(scaled_data[i - base_days:i])
    y_data.append(scaled_data[i])

x_data = np.array(x_data)
y_data = np.array(y_data)

# Reshape x_data to be 3D for LSTM
x_data = np.reshape(x_data, (x_data.shape[0], x_data.shape[1], 1))

#Split the data to train and test
train_size = int(len(x_data) * 0.9)
x_train, y_train = x_data[:train_size], y_data[:train_size]
x_test, y_test = x_data[train_size:], y_data[train_size:]

#Creating the LSTM model
model = Sequential([
    LSTM(128, return_sequences = True, input_shape = (x_train.shape[1], 1)),
    LSTM(64, return_sequences = False ),
    Dense(25),
    Dense(1)
])

model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(x_train, y_train, batch_size=5, epochs=3)

# Save model
folder_name = 'model'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

model_file_path = os.path.join(folder_name, 'model_final.h5')
model.save(model_file_path)