from backtesting import Backtest
import pandas as pd

from RsiOscillator import RsiOscillator
from SmaCross import SmaCross


df = pd.read_csv("stock_data_genxil.csv", index_col='Time', parse_dates=True)

#print(df)

bt = Backtest(df, SmaCross, cash=100000, commission=.0035,
              exclusive_orders=True)
# For Rsi Indicator
# stats = bt.optimize(
#         upper_bound=range(50, 85, 5),
#         lower_bound=range(10, 40, 5),
#         rsi_window=range(10, 30, 2),
#         maximize='Return [%]')

# For SMA Cross. n1 should not be larger than or equal to n2
stats = bt.optimize(n1=range(5, 30, 3),
                    n2=range(10, 70, 5),
                    #constraint=lambda x: x.n2 - x.n1 > 20,
                    constraint=lambda param: param.n1 < param.n2,
                    maximize='Sharpe Ratio')

#stats = bt.run()
print(stats.to_string())
#print(stats['_trades'].to_string())
bt.plot()

