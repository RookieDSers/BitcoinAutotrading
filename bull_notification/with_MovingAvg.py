import pybithumb
import datetime
import time

from pybithumb.client import Bithumb

keys = []
with open('/Volumes/SteveJobs/localGit/bitcoin_tutorial/bithumbKey.txt') as f:
    keys = f.readlines()
bithumb = pybithumb.Bithumb(keys[0].strip(), keys[1].strip())


def get_target_price(ticker):
    # calculate target price
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target


def buy_crypto_currency(ticker):
    # buy crypto currency with volatility breakout strategy
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw / float(sell_price)
    bithumb.buy_market_order(ticker, unit)


def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)


def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]


now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
ma5 = get_yesterday_ma5("BTC")
target_price = get_target_price("BTC")

while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(seconds=10):
            # renew target price every midnight
            target_price = get_target_price("BTC")
            mid = datetime.datetime(now.year, now.month,
                                    now.day) + datetime.timedelta(1)
            ma5 = get_yesterday_ma5("BTC")
            sell_crypto_currency("BTC")

        current_price = pybithumb.get_current_price("BTC")
        if (current_price > target_price) and (current_price > ma5):
            # buy market order when current price is higher than target_price
            buy_crypto_currency("BTC")
    except:
        print("Error Occured!")
    time.sleep(1)
