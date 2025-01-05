from matplotlib import pyplot as plt
import pandas as pd
import train


predictions = train.model.predict(train.x_test)
inv_predictions = train.scaler.inverse_transform(predictions)
inv_y_test = train.scaler.inverse_transform(train.y_test)

plotting_data =  pd.DataFrame(
    {
        'Original': inv_y_test.flatten(),
        'predictions': inv_predictions.flatten(),
    }, index = train.close_prices.index[train.train_size + train.base_days:]
)

# Plot Closing price with Moving Averages
plt.figure(figsize=(15, 6))
plt.plot(plotting_data.index, plotting_data['Original'], label='Original', color='Blue', linewidth=2)
plt.plot(plotting_data.index, plotting_data['predictions'], label='Prediction', color='Red', linewidth=2)
plt.title('Prediction vs Actual Close Price', fontsize=16)
plt.xlabel('Years', fontsize=14)
plt.ylabel('Close Price', fontsize=14)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show() 