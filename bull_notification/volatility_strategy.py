import pybithumb

# Calculate Range and Base Price with K=0.5
df = pybithumb.get_ohlcv("BTC")
yesterday = df.iloc[-2]
today_open = yesterday['close']
yesterday_high = yesterday['high']
yesterday_low = yesterday['low']
base = today_open + (yesterday_high - yesterday_low) * 0.5
print(base)

# Bull notification
price = pybithumb.get_current_price("BTC")

if price > base:
    print("Bull!!!")
else:
    print("Bear...")

# Define Bull notification function
def vol_bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    base = today_open + (yesterday_high - yesterday_low) * 0.5
    price = pybithumb.get_current_price(ticker)
    if price > base:
        return True
    else:
        return False

tickers = pybithumb.get_tickers()
for ticker in tickers:
    is_bull = vol_bull_market(ticker)
    if is_bull:
        print(ticker, " is Bull!!!")
    else:
        print(ticker, " is Bear...")
