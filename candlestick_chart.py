import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

#Define Time Frame
start = dt.datetime(2026, 7, 6)
end = dt.datetime.now()

#Load Data
data = yf.download("TCS.NS", start=start, end=end, multi_level_index=False)
if data is None or data.empty:
    raise ValueError("No data returned from yf.download")

# Restructure Data
data = data[['Open', 'High', 'Low', 'Close']]
data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)
print(data.head())

# Visualization 
ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('TCS Share Price', color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width=0.6, colorup='#00ff00', colordown='red')

plt.show()