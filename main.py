from backtesting import Backtest
import pandas as pd

from RsiOscillator import RsiOscillator
from SmaCross import SmaCross
from RsiDivergence import RSIStrategy

df = pd.read_csv("stock_data_bpml.csv", index_col='Time', parse_dates=True)

# print(df)

bt = Backtest(df, RsiOscillator, cash=100000, commission=.0035,
              exclusive_orders=True)

stats = bt.optimize(
        upper_bound=range(50, 85, 5),
        lower_bound=range(10, 45, 5),
        rsi_window=range(10, 30, 2),
        maximize='Sharpe Ratio')

#stats = bt.run()
print(stats)
bt.plot()

