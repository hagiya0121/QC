from AlgorithmImports import *
from future_symbols import future_symbols
from CustomUniverseSelectionModel import (
    RandomContinuousFutureUniverseSelectionModel,
)


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
            RandomContinuousFutureUniverseSelectionModel(
                period=1, sample_size=5, future_symbols=future_symbols()
            )
        )

    def on_data(self, data: Slice) -> None:
        self.debug(f"{self.time}: === On Data ===")
        self.debug(f"Count: {len(self.active_securities)}")
        for kvp in self.active_securities:
            if kvp.key.is_canonical():
                self.debug(f"Symbol: {kvp.key} Mapped: {kvp.value.mapped}")
