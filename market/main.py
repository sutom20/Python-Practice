import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(stock_symbol):
    try:
        # Fetch stock data for the specified symbol
        stock_data = yf.download(stock_symbol, start='2023-01-01', end='2024-02-29')

        # Calculate 14-period RSI
        delta = stock_data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        RS = gain / loss
        RSI = 100 - (100 / (1 + RS))

        # Create a single plot for stock closing price and RSI
        fig, ax1 = plt.subplots(figsize=(20, 10))

        # Plot stock closing price on the left Y-axis
        ax1.plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')
        ax1.set_ylabel('Close Price', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')
        ax1.legend(loc='upper left')

        # Create a second Y-axis for RSI
        ax2 = ax1.twinx()

        # Plot RSI on the right Y-axis
        ax2.plot(stock_data.index, RSI, label='14-Period RSI', color='white')
        ax2.set_ylabel('RSI', color='orange')
        ax2.tick_params(axis='y', labelcolor='orange')
        ax2.legend(loc='upper right')

        # Plot RSI zone lines
        ax2.axhline(y=30, color='red', linestyle='--', label='Oversold Zone')
        ax2.axhline(y=70, color='green', linestyle='--', label='Overbought Zone')

        # Fill areas above RSI 70 and below RSI 30
        ax2.fill_between(stock_data.index, RSI, 70, where=(RSI >= 70), color='coral', alpha=0.5)
        ax2.fill_between(stock_data.index, RSI, 30, where=(RSI <= 30), color='green', alpha=0.5)

        plt.title(f'Performance of {stock_symbol} over the Years')
        plt.grid(False)
        plt.show()

        # Save the data to a CSV file (optional)
        stock_data.to_csv(f"{stock_symbol}_stock_data.csv")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Get user input for the stock symbol
    symbol = input("Enter the stock symbol (e.g., INFY.NS): ")

    # Fetch stock data for the specified symbol
    fetch_stock_data(symbol)
