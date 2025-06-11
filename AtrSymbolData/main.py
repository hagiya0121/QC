from AlgorithmImports import *


class AtrSymbolDataAlgorithm(QCAlgorithm):
    def initialize(self):
        self.set_start_date(2023, 1, 1)
        self.set_end_date(2023, 6, 1)
        self.set_cash(100000)

        self.symbol_data = {}

        tickers = ["ES", "CL", "GC"]
        for ticker in tickers:
            future = self.add_future(ticker, Resolution.DAILY)
            continuous_symbol = future.symbol

            sd = SymbolData(self, continuous_symbol)
            self.symbol_data[continuous_symbol] = sd

    def on_data(self, data: Slice):
        self.debug(f"{self.time} === ATR ===")
        for symbol, sd in self.symbol_data.items():
            if sd.is_ready:
                self.plot("ATR", symbol, sd.value)

            if sd.is_ready:
                self.debug(f"Symbol: {symbol}, ATR: {sd.value:.2f}")


class SymbolData:
    def __init__(self, algorithm: QCAlgorithm, symbol: Symbol, period: int = 14):
        self.symbol = symbol
        self.algorithm = algorithm
        self.period = period

        self.atr = algorithm.atr(symbol, period, MovingAverageType.SIMPLE)

        history = algorithm.history[TradeBar](symbol, period + 1, Resolution.DAILY)
        for bar in history:
            self.atr.update(bar)

    @property
    def is_ready(self):
        return self.atr.is_ready

    @property
    def value(self):
        return self.atr.current.value if self.atr.is_ready else None
