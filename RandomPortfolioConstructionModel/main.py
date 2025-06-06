from AlgorithmImports import *  # type: ignore[reportWildcardImportFromLibrary]
import random
from datetime import timedelta


class RandomPortfolioConstructionAlgorithm(QCAlgorithm):
    def initialize(self):
        self.set_start_date(2013, 1, 1)
        self.set_end_date(2013, 1, 31)
        self.set_cash(100000)

        self.symbols = [
            self.add_equity("AAPL", Resolution.DAILY).symbol,
            self.add_equity("MSFT", Resolution.DAILY).symbol,
            self.add_equity("GOOGL", Resolution.DAILY).symbol,
        ]

        self.set_universe_selection(ManualUniverseSelectionModel(self.symbols))
        self.add_alpha(
            ConstantAlphaModel(InsightType.PRICE, InsightDirection.UP, timedelta(1))
        )
        self.set_portfolio_construction(RandomWeightingPortfolioConstructionModel())


class RandomWeightingPortfolioConstructionModel(PortfolioConstructionModel):
    def create_targets(
        self, algorithm: QCAlgorithm, insights: list[Insight]
    ) -> list[PortfolioTarget]:
        if not insights:
            return []

        n = len(insights)
        raw_weights = [random.random() for _ in range(n)]
        total = sum(raw_weights)
        weights = [w / total for w in raw_weights]

        targets = []
        for insight, weight in zip(insights, weights):
            targets.append(PortfolioTarget.percent(algorithm, insight.symbol, weight))

        self._log_portfolio_targets(algorithm, targets)

        return targets

    def _log_portfolio_targets(
        self, algorithm: QCAlgorithm, targets: list[PortfolioTarget]
    ) -> None:
        algorithm.debug("=== Portfolio Targets ===")
        for target in targets:
            symbol = target.symbol
            quantity = target.quantity
            price = algorithm.securities[symbol].price
            total_value = quantity * price

            algorithm.debug(
                f"Symbol: {target.symbol}, Quantity: {target.quantity}, $: {total_value:.2f}"
            )
