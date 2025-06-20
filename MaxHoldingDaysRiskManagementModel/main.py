from AlgorithmImports import *
from datetime import timedelta


class MaxHoldingDaysRiskManagementAlgorithm(QCAlgorithm):
    def initialize(self):
        self.set_start_date(2013, 10, 8)
        self.set_end_date(2013, 10, 15)
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
        self.set_portfolio_construction(FixedQuantityPortfolioConstructionModel())
        self.add_risk_management(MaxHoldingDaysRiskManagementModel(max_days=3))

    def on_data(self, data: Slice):
        pass


class MaxHoldingDaysRiskManagementModel(RiskManagementModel):
    def __init__(self, max_days=2):
        self.max_days = max_days
        self.holding_days = {}

    def manage_risk(self, algorithm, targets):
        risk_adjusted_targets = []

        self._log_position(algorithm)

        for symbol, holding in algorithm.portfolio.items():
            if not holding.invested:
                continue

            if symbol not in self.holding_days:
                self.holding_days[symbol] = 0

            self.holding_days[symbol] += 1

            if self.holding_days[symbol] >= self.max_days:
                risk_adjusted_targets.append(PortfolioTarget(symbol, 0))
                self.holding_days.pop(symbol, None)

        return risk_adjusted_targets

    def _log_position(self, algorithm):
        algorithm.debug(f"{algorithm.time} === Position Log ===")
        if not any(h.invested for h in algorithm.portfolio.values()):
            algorithm.debug("No open positions.")
            return

        for symbol, holding in algorithm.portfolio.items():
            if holding.invested:
                algorithm.debug(
                    f"Symbol: {symbol}, holding_days: {self.holding_days.get(symbol, 0) + 1}"
                )


class FixedQuantityPortfolioConstructionModel(PortfolioConstructionModel):
    def __init__(self, fixed_quantity=100):
        super().__init__()
        self.fixed_quantity = fixed_quantity

    def create_targets(
        self, algorithm: QCAlgorithm, insights: list[Insight]
    ) -> list[PortfolioTarget]:
        if not insights:
            return []

        targets = []
        for insight in insights:
            targets.append(PortfolioTarget(insight.symbol, self.fixed_quantity))

        return targets
