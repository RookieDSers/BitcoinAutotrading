import numpy as np
import pybithumb

df = pybithumb.get_ohlcv("BTC")
df = df['2021']
df['ma5'] = df['close'].rolling(5).mean().shift(1)
df['range'] = (df['high']-df['low'])*0.7
df['target'] = df['open']+df['range'].shift(1)
df['bull'] = df['open'] > df['ma5']

fee = 0.0032
df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                     df['close']/df['target'] - fee, 1)
# calculate hpr
df['hpr'] = df['ror'].cumprod()

# calculate dd
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
print("HPR: ", df['hpr'][-2])
df.to_excel("btc_larry_ma.xlsx")
