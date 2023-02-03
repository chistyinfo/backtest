from backtesting import Strategy
from backtesting.lib import crossover
from backtesting.test import SMA

class ChistyTriangle(Strategy):
    n1 = 9
    n2 = 20

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            if self.position.is_short or not self.position:
                self.position.close()
            self.sell()
