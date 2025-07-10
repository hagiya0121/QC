from AlgorithmImports import *
from Logger import Logger
from future_symbols import future_symbols
from CustomUniverseSelectionModel import (
    RandomContinuousFutureUniverseSelectionModel,
)


class RandomContinuousFutureUniverseAlgorithm(QCAlgorithm):
    def initialize(self) -> None:
        self.set_start_date(2022, 1, 1)
        self.set_end_date(2022, 4, 30)
        self.set_cash(100000)

        self.logger = Logger(algorithm=self)

        self.universe_settings.asynchronous = False
        self.universe_settings.extended_market_hours = True
        self.universe_settings.resolution = Resolution.DAILY
        self.universe_settings.data_mapping_mode = DataMappingMode.OPEN_INTEREST
        self.universe_settings.data_normalization_mode = (
            DataNormalizationMode.BACKWARDS_RATIO
        )
        self.add_universe_selection(
            RandomContinuousFutureUniverseSelectionModel(
                period=3,
                sample_size=4,
                future_symbols=future_symbols(),
            )
        )

    def on_data(self, data: Slice) -> None:
        self.logger.log_if_canonical_changed()
