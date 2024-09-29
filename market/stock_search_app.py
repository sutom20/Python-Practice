import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def fetch_and_plot_stock_data():
    stock_symbol = stock_symbol_entry.get()

    try:
        if not stock_symbol:
            raise ValueError("Please enter a valid stock symbol.")

        # Fetch stock data for the specified symbol
        stock_data = yf.download(stock_symbol, start='2024-01-01', end='2024-02-29')

        # Plot the daily close price
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data.index, stock_data['Close'], label='Close Price')
        plt.title(f'Daily Close Price of {stock_symbol}')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.legend()
        plt.grid(True)

        # Display the plot on the tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the tkinter window
window = tk.Tk()
window.title("Stock Data Visualization")
window.configure(bg="white")  # Set background color to white

# Set a fixed size for the tkinter window
window.geometry("600x400")

# Create an entry field for entering the stock symbol
stock_symbol_entry = tk.Entry(window)
stock_symbol_entry.pack()

# Create a button to fetch and plot the stock data
fetch_button = tk.Button(window, text="Fetch and Plot Data", command=fetch_and_plot_stock_data, bg="black", fg="white")
fetch_button.pack()

# Run the tkinter event loop
window.mainloop()
