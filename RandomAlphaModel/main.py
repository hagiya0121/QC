from AlgorithmImports import *
from Logger import Logger
from CustomAlphaModel import RandomAlphaModel
from FutureSymbols import future_symbols
from CustomUniverseSelectionModel import RandomContinuousFutureUniverseSelectionModel


class RandomAlphaModelAlgorithm(QCAlgorithm):
    def initialize(self):
        self.set_start_date(2020, 1, 1)
        self.set_end_date(2020, 12, 31)
        self.set_cash(100000)
        self.logger = Logger(self)

        self.universe_settings.asynchronous = False
        self.universe_settings.extended_market_hours = True
        self.universe_settings.resolution = Resolution.DAILY
        self.universe_settings.data_mapping_mode = DataMappingMode.OPEN_INTEREST
        self.universe_settings.data_normalization_mode = (
            DataNormalizationMode.BACKWARDS_RATIO
        )
        self.add_universe_selection(
            RandomContinuousFutureUniverseSelectionModel(
                period=10,
                sample_size=5,
                future_symbols=future_symbols(),
            )
        )
        self.add_alpha(RandomAlphaModel(period=3))

    def on_data(self, data: Slice) -> None:
        self.logger.log_if_canonical_changed()
        self.logger.log_insights()
