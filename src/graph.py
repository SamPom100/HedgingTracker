import yfinance as yf
import matplotlib.pyplot as plt

ticker = "AAPL"
stock = yf.Ticker(ticker)
current_price = stock.info['currentPrice']

option_dates = stock.options

for date in option_dates:
    option_chain = stock.option_chain(date)
    plt.plot(option_chain.calls['strike'], option_chain.calls['openInterest'])

plt.axvline(x=current_price, color='r', linestyle='dashed')
plt.legend(option_dates)
plt.show()