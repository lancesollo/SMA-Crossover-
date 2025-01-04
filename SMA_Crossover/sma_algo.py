import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Parameters for the strategy
short_window = 20  # Short-term SMA
long_window = 50   # Long-term SMA
ticker = "AAPL"    # Example stock ticker (Apple)
start_date = "2020-01-01"
end_date = "2023-01-01"

# Step 1: Fetch historical data
print("Downloading data...")
data = yf.download(ticker, start=start_date, end=end_date)

# Step 2: Calculate SMAs
data['SMA_Short'] = data['Close'].rolling(window=short_window).mean()
data['SMA_Long'] = data['Close'].rolling(window=long_window).mean()

# Step 3: Define trading signals
data['Signal'] = 0  # No position initially
data.loc[data['SMA_Short'] > data['SMA_Long'], 'Signal'] = 1  # Buy signal
data.loc[data['SMA_Short'] <= data['SMA_Long'], 'Signal'] = -1  # Sell signal

# Step 4: Backtest the strategy
# Calculate returns
data['Daily_Return'] = data['Close'].pct_change()
data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']  # Lagging signal

# Step 5: Plotting
plt.figure(figsize=(12, 8))

# Plot the closing price and SMAs
plt.plot(data['Close'], label="Close Price", alpha=0.5)
plt.plot(data['SMA_Short'], label=f"{short_window}-Day SMA", alpha=0.75)
plt.plot(data['SMA_Long'], label=f"{long_window}-Day SMA", alpha=0.75)

# Plot buy and sell signals
plt.scatter(data[data['Signal'] == 1].index, data[data['Signal'] == 1]['Close'], label="Buy Signal", marker="^", color="green")
plt.scatter(data[data['Signal'] == -1].index, data[data['Signal'] == -1]['Close'], label="Sell Signal", marker="v", color="red")

plt.title(f"SMA Crossover Strategy for {ticker}")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()

# Step 6: Performance Metrics
total_return = (1 + data['Strategy_Return']).prod() - 1
print(f"Total Strategy Return: {total_return:.2%}")
