import yfinance as yf

ticker = yf.Ticker("ADLABS.NS")

print(ticker.history(period="5d"))
print(ticker.info.get("longName"))