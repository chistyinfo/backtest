from backtesting import Backtest
from backtesting import Strategy
import pandas as pd


# Load the stock data into a DataFrame


class Start(Strategy):

    def init(self):
        pass

    # Step through bars one by one
    def next(self):
        price = self.data.Close[-1]

        if self.position:
            pass
        else:
            # Look at _Broker class for details on order processing
            # What happens when we have sl and tp, etc.
            self.buy(size=1, sl=price - 5, tp=price + 10)
