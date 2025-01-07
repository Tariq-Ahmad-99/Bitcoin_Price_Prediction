
# Crypto Production Project Documentation

## Project Overview
This project involves predicting cryptocurrency prices using an LSTM model and deploying the model through a Flask web application. The project uses Bitcoin (BTC-USD) as the primary example for cryptocurrency price predictions.

## Features
- **LSTM Model for Price Prediction:**
  - Trains an LSTM model on historical cryptocurrency data.
  - Uses Yahoo Finance API to fetch the data.
  - Predicts future prices based on past trends.

- **Flask Web Application:**
  - Allows users to input a stock ticker and number of days for future predictions.
  - Generates visualizations for original data, predicted data, and future price predictions.

## Technology Stack
- **Backend:**
  - Python
  - Flask
  - Keras (with TensorFlow backend)
  - Yahoo Finance API (yfinance)
  - Scikit-learn
  - Matplotlib

- **Frontend:**
  - HTML Templates (rendered via Flask)
  - Bootstrap (for styling)

## Setup Instructions
### Prerequisites
- Python 3.x
- Pip (Python package manager)

### Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/crypto-prediction-project.git
   cd crypto-prediction-project
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. **Train the Model:**
   - Ensure the `model` folder exists in the project root.
   - Run the LSTM training script to generate `model_final.h5` and `data.pkl` files.

2. **Start the Flask Server:**
   ```bash
   python app.py
   ```
   - The application will be accessible at `http://127.0.0.1:5000/`.

### Usage
1. Navigate to the application URL.
2. Input a stock ticker symbol (default is `BTC-USD`).
3. Enter the number of days for future price predictions.
4. View the generated plots and predictions.

## Project Structure
```
crypto-prediction-project/
├── app.py                  # Flask application
├── model/
│   ├── model_final.h5      # Trained LSTM model
│   └── data.pkl            # Scaled data and other necessary variables
├── templates/
│   ├── index.html          # Home page template
│   └── result.html         # Result page template
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Future Enhancements
- Add more cryptocurrencies and stock tickers for broader predictions.
- Enhance the UI with more interactive elements.
- Implement advanced error handling and logging.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For further assistance or to report issues, please contact me.
