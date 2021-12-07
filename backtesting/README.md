## Backtesting


### Prepare backtesting data
1. Prepare backtesting excel data with Bitcoin information
```python
import pybithumb

df = pybithumb.get_ohlcv("BTC")
df.to_excel("btc.xlsx")
```

### Volatility breakout strategy and bull market backtesting in python codes
1. Calculate range with k value and target price based on yesterday's range
```python
df = df['2021']
df['range'] = (df['high']-df['low'])*0.5
df['range_shift1'] = df['range'].shift(1)
df['target'] = df['open']+df['range'].shift(1)
```
2. Calculate five days moving average and define bull market 
```python
df['ma5'] = df['close'].rolling(5).mean().shift(1)
df['bull'] = df['open'] > df['ma5']
```

4. Calculate Rates Of Return (ROR) considering fee
```python
import numpy
fee = 0.0032
df['ror'] = np.where((df['high'] > df['target']),
                     df['close']/df['target'] - fee, 1)
```
4. Calculate Holding Period Return (HPR)
```python
df['hpr'] = df['ror'].cumprod()
print("HPR: ", df['hpr'][-2])
```
5. Calculate Maximum Draw Down (MDD)
```python
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
```
6. Make the final excel data with the above codes 
```python
import numpy as np
import pybithumb

df = pybithumb.get_ohlcv("BTC")
df = df['2021']
df['ma5'] = df['close'].rolling(5).mean().shift(1)
df['range'] = (df['high']-df['low'])*0.5
df['target'] = df['open']+df['range'].shift(1)
df['bull'] = df['open'] > df['ma5']

fee = 0.0032
df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                     df['close']/df['target'] - fee, 1)


df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
print("HPR: ", df['hpr'][-2])
df.to_excel("btc_larry_ma.xlsx")
```
### Find best k value
- Best k value is the value that maximizes the Rates of Return (ROR)

1. Define a function calculating ror
```python
import pybithumb
import numpy as np

def get_ror(k=0.5):
    df['range'] = (df['high']-df['low'])*k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close']/df['target']-fee, 1)
    ror = df['ror'].cumprod()[-2]
    return ror
```
2. Iterate over the k-values from 0.1 to 0.9 and calculate ror based on each k values by using the above function.
```python
for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))
```
### Find best ticker
- Best ticker refers to the cryptocurrency that has the highest Holding Period Return in 2021.
1. Define a function calculating HPR of ticker in 2021 based on above codes
```python
def get_hpr(ticker):
    try:
        df = pybithumb.get_ohlcv(ticker)
        df = df.loc['2021']

        df['ma5'] = df['close'].rolling(5).mean().shift(1)
        df['range'] = (df['high']-df['low']) * 0.7
        df['target'] = df['open'] + df['range'].shift(1)
        df['bull'] = df['open'] > df['ma5']

        fee = 0.0032
        df['ror'] = np.where((df['high'] > df['target']) &
                             df['bull'], df['close']/df['target']-fee, 1)
        df['hpr'] = df['ror'].cumprod()
        df['dd'] = (df['hpr'].cummax()-df['hpr'])/df['hpr'].cummax()*100
        return df['hpr'][-2]
    except:
        return 1
```
2. Find top five tickers in 2021
```python
tickers = pybithumb.get_tickers()

hprs = []
for ticker in tickers:
    hpr = get_hpr(ticker)
    hprs.append((ticker, hpr))

sorted_hprs = sorted(hprs, key=lambda x: x[1], reverse=True)
print(sorted_hprs[:5])
```

