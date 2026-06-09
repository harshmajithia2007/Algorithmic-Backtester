import pandas as pd
import yfinance as yf

# Fetch 10 years of historical data for Apple(AAPL)
stock = yf.Ticker("AAPL").history(period="10y")

# Calculate the 50-day and 200-day Simple Moving Averages (SMA)
stock["SMA_50"] = stock["Close"].rolling(window=50).mean()
stock["SMA_200"] = stock["Close"].rolling(window=200).mean()

# Strip out unnecessary columns to keep the dataframe clean
stock = stock.drop(columns=["Volume", "Dividends", "Stock Splits", "Open", "High", "Low"])

# Generate trading signals: 1 when the 50 SMA is above the 200 SMA (Bullish), otherwise 0
stock["Signal"] = (stock["SMA_50"] >= stock["SMA_200"]).astype(int)

# Shift signals by 1 day to avoid lookahead bias, then calculate daily returns
stock["Position"] = stock["Signal"].shift(1)
stock["Market_Returns"] = stock["Close"].pct_change()
stock["Strategy_Returns"] = stock["Market_Returns"] * stock["Position"]

# Compound the returns over time to get cumulative performance
stock["Cumulative Market Returns"] = ((stock["Market_Returns"] + 1).cumprod(axis=0, skipna=True))
stock["Cumulative Strategy Returns"] =((stock["Strategy_Returns"] + 1).cumprod(axis=0, skipna=True))

# Track the running peak wealth to measure risk exposure
peak_market = stock["Cumulative Market Returns"].cummax()
peak_strategy = stock["Cumulative Strategy Returns"].cummax()

# Measure the daily peak-to-trough drops (drawdowns)
drawdown_market = (stock["Cumulative Market Returns"] - peak_market) / peak_market
drawdown_strategy = (stock["Cumulative Strategy Returns"] - peak_strategy) / peak_strategy

# Extract the worst-case historical drop for both approaches
max_dd_market = drawdown_market.min()
max_dd_strategy = drawdown_strategy.min()

# Grab the final compounded return values
final_market = stock["Cumulative Market Returns"].iloc[-1]
final_strategy = stock["Cumulative Strategy Returns"].iloc[-1]

# Display the performance breakdown
print("----------------------")
print("Algorithmic Backtester")
print("----------------------")
print(f"Market Returns: {final_market:.4f}")
print(f"Strategy Returns: {final_strategy:.4f}")
print("-----------------------------")
print(f"Market Max Drawdown: {max_dd_market * 100:.2f}%")
print(f"Strategy Max Drawdown: {max_dd_strategy * 100:.2f}%")
print("-----------------------------")

# Determine the winning approach based on final returns
if final_market >= final_strategy:
    print("Verdict: It is better to buy and hold the stock")
else:
    print("Verdict: It is better to follow the SMA strategy")
print("-----------------------------")