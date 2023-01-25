from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import pandas as pd


class RSIStrategy(Strategy):
    def init(self):
        # Define the RSI indicator
        self.rsi = self.data.RSI()

    def next(self):
        # Check for RSI divergence
        if crossover(self.data.price, self.rsi):
            self.buy()
        elif crossover(self.rsi, self.data.price):
            self.sell()
