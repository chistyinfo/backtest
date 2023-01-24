from backtesting import Backtest
import pandas as pd

from RsiOscillator import RsiOscillator
from SmaCross import SmaCross

df = pd.read_csv("stock_data_bpml.csv", index_col='Time', parse_dates=True)

# print(df)

bt = Backtest(df, SmaCross, cash=100000, commission=.0035,
              exclusive_orders=True)

stats = bt.run()
print(stats)
#bt.plot()


