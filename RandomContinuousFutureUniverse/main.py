from AlgorithmImports import *
from Selection.FutureUniverseSelectionModel import FutureUniverseSelectionModel
from datetime import timedelta, datetime
import random
from future_symbols import future_symbols


class RandomContinuousFutureUniverseAlgorithm(QCAlgorithm):
    def initialize(self) -> None:
        self.set_start_date(2022, 1, 1)
        self.set_end_date(2022, 12, 31)
        self.set_cash(100000)

        self.universe_settings.asynchronous = True
        self.universe_settings.extended_market_hours = True
        self.universe_settings.resolution = Resolution.DAILY
        self.universe_settings.data_mapping_mode = DataMappingMode.OPEN_INTEREST
        self.universe_settings.data_normalization_mode = (
            DataNormalizationMode.BACKWARDS_RATIO
        )
        self.add_universe_selection(
            RandomContinuousFutureUniverseSelectionModel(period=1, sample_size=5)
        )

    def on_data(self, data: Slice) -> None:
        self.debug(f"{self.time}: === On Data ===")
        self.debug(f"Count: {len(self.active_securities)}")
        for kvp in self.active_securities:
            if kvp.key.is_canonical():
                self.debug(f"Symbol: {kvp.key} Mapped: {kvp.value.mapped}")


class RandomContinuousFutureUniverseSelectionModel(FutureUniverseSelectionModel):
    def __init__(self, period=1, sample_size=1) -> None:
        self.sample_size = sample_size
        super().__init__(timedelta(period), self.select_continuous_future_symbols)

    def select_continuous_future_symbols(self, utc_time: datetime) -> list[Symbol]:
        return random.sample(future_symbols(), self.sample_size)

    def filter(self, filter: FutureFilterUniverse) -> FutureFilterUniverse:
        return filter.none()
