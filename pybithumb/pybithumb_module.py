import pybithumb
import time
import datetime

# get tickers
tickers = pybithumb.get_tickers()
print(tickers)
print(len(tickers))

# get current price
price = pybithumb.get_current_price("BTC")
print(f'BTC: {price}')

# market details
detail = pybithumb.get_market_detail("BTC")
print('market price, high, low, current')
print(detail)

# current price of tickers
# for ticker in tickers:
#     price = pybithumb.get_current_price(ticker)
#     print(f'{ticker}: {price}')
#     time.sleep(0.1)

# get asks and bids
orderbook = pybithumb.get_orderbook("BTC")
print(orderbook)
bids = orderbook['bids']
asks = orderbook['asks']
print('bids:')
for bid in bids:
    print(bid)

# printing timestamp
ms = int(orderbook['timestamp'])
dt = datetime.datetime.fromtimestamp(ms/1000)
print(dt)
