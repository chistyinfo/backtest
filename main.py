from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA

import pandas as pd

# Load the stock data into a DataFrame
from stop_loss import Start

df = pd.read_csv("stock_data_g.csv", index_col='Time', parse_dates=True)


# print(df)


class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 9)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


Start
# Backtest for stop loss
bt = Backtest(df, Start, cash=100000, commission=.0035,
              exclusive_orders=True)

# Backtest sma cross over
ct = Backtest(df, SmaCross, cash=100000, commission=.0035,
              exclusive_orders=True)

stats = bt.run()
tats = ct.run()
print(stats, tats)
bt.plot()
ct.plot()
