from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas_ta as ta

import pandas as pd



class RSIStrategy(Strategy):
    def init(self):
        # Define the RSI indicator
        self.rsi = self.I(ta.rsi, self.data.close, 14)

    def next(self):
        # Check for RSI divergence
        if crossover(self.data.close, self.rsi):
            self.buy()
        elif crossover(self.rsi, self.data.close):
            self.sell()




