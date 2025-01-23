# SMA-Crossover-

This algorithm is a Simple Moving Average Algorithm. What it does is averages price over a specified period. For this example, I used Apple ("AAPL") to test the algorithm. 

The SMA is only used for educational purposes, as a benchmark to learning about Quantitative Trading & Research.


### How It Works:

1. **Data Collection**: Fetches historical price data for the specified stock using `yfinance`.
2. **SMA Calculation**: Computes short-term and long-term SMAs based on the rolling window parameters.
3. **Signal Generation**:
    - Buy when the short SMA crosses above the long SMA.
    - Sell when the short SMA crosses below the long SMA.
4. **Backtest**: Simulates the strategy by applying trading signals to historical returns.
5. **Visualization**: Plots the stock's price, SMAs, and trading signals.
