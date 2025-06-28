from AlgorithmImports import *
from Selection.FutureUniverseSelectionModel import FutureUniverseSelectionModel
from datetime import timedelta, datetime
import random


class RandomContinuousFutureUniverseSelectionModel(FutureUniverseSelectionModel):
    def __init__(self, period=1, sample_size=1, future_symbols=None) -> None:
        self.sample_size = sample_size
        self.future_symbols = future_symbols or []
        super().__init__(timedelta(period), self.select_continuous_future_symbols)

    def select_continuous_future_symbols(self, utc_time: datetime) -> list[Symbol]:
        return random.sample(self.future_symbols, self.sample_size)

    def filter(self, filter: FutureFilterUniverse) -> FutureFilterUniverse:
        return filter.expiration(0, 0)
