import yfinance as yf

# Define the stock ticker
ticker = "RHM.DE"

# Download historical data
rhm = yf.Ticker(ticker)
history = rhm.history(period="5y", interval="1d") # Fetch past 1 year of data

# Display the first few rows
print(history.head())

import matplotlib.pyplot as plt

# Plot closing prices
history["Close"].plot(title="Rheinmetall AG (RHM.DE) Stock Price", figsize=(10, 5))
plt.xlabel("Date")
plt.ylabel("Stock Price (€)")
plt.show()

print(rhm.info)