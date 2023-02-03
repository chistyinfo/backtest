import pandas as pd
import ta.trend
from backtesting import Strategy
from backtesting.lib import crossover


class SmaCross(Strategy):
    n1 = 9
    n2 = 20

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(ta.trend.sma_indicator, pd.Series(close), self.n1)
        self.sma2 = self.I(ta.trend.sma_indicator, pd.Series(close), self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            if self.position.is_long:
                self.position.close()
                self.buy()
        elif crossover(self.sma2, self.sma1):
            if self.position.is_short or not self.position:
                self.position.close()
                self.sell()
