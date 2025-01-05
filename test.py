from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import pickle
from tensorflow.keras.models import load_model # type: ignore

model = load_model('model/model_final.h5')
# Load the saved data
with open('model/data.pkl', 'rb') as f:
    data = pickle.load(f)

x_test = data['x_test']
y_test = data['y_test']
scaler = data['scaler']
scaled_data = data['scaled_data']
close_prices = data['close_prices']
train_size = data['train_size']
base_days = data['base_days']

predictions = model.predict(x_test)
inv_predictions = scaler.inverse_transform(predictions)
inv_y_test = scaler.inverse_transform(y_test)

plotting_data =  pd.DataFrame(
    {
        'Original': inv_y_test.flatten(),
        'predictions': inv_predictions.flatten(),
    }, index = close_prices.index[train_size + base_days:]
)

# Prediction vs Actual Close Price
""" plt.figure(figsize=(15, 6))
plt.plot(plotting_data.index, plotting_data['Original'], label='Original', color='Blue', linewidth=2)
plt.plot(plotting_data.index, plotting_data['predictions'], label='Prediction', color='Red', linewidth=2)
plt.title('Prediction vs Actual Close Price', fontsize=16)
plt.xlabel('Years', fontsize=14)
plt.ylabel('Close Price', fontsize=14)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()  """

last_100 = scaled_data[-100:].reshape(1, -1, 1) 
future_predictions = []

for _ in range(10):
    next_days = model.predict(last_100)  # Predict the next value
    future_predictions.append(scaler.inverse_transform(next_days))  # Inverse transform to get the original scale
    last_100 = np.append(last_100[:, 1:, :], next_days.reshape(1, 1, -1), axis=1)

# Flatten the list of future predictions for plotting
future_predictions = np.array(future_predictions).flatten()

# Plot the future predictions
plt.figure(figsize=(15, 6))
plt.plot(range(1, 11), future_predictions, marker="o", label='Prediction Future Prices', color='purple', linewidth=2)

for i, val in enumerate(future_predictions):
    plt.text(i + 1, val, f'{val:.2f}', fontsize=10, ha='center', va='bottom', color='black')

plt.title('Future Close Prices for 10 days', fontsize=16)
plt.xlabel('Days', fontsize=14)
plt.ylabel('Close Price', fontsize=14)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()
