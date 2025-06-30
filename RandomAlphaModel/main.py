from AlgorithmImports import *
from CustomAlphaModel import RandomAlphaModel


class RandomAlphaModelAlgorithm(QCAlgorithm):
    def initialize(self):
        self.set_start_date(2020, 1, 1)
        self.set_end_date(2020, 12, 31)
        self.set_cash(100000)

        self.add_future(Futures.Grains.CORN, Resolution.DAILY)
        self.add_future(Futures.Grains.SOYBEANS, Resolution.DAILY)
        self.add_future(Futures.Grains.SOYBEAN_OIL, Resolution.DAILY)

        self.add_alpha(RandomAlphaModel(period=3, log_insights=True))
