from AlgorithmImports import *  # type: ignore[reportWildcardImportFromLibrary]
from datetime import timedelta
import random


class RandomAlphaModelAlgorithm(QCAlgorithm):
    def initialize(self):
        self.set_start_date(2020, 1, 1)
        self.set_end_date(2020, 12, 31)
        self.set_cash(100000)

        self.add_future(Futures.Grains.CORN, Resolution.DAILY)
        self.add_future(Futures.Grains.SOYBEANS, Resolution.DAILY)
        self.add_future(Futures.Grains.SOYBEAN_OIL, Resolution.DAILY)

        self.add_alpha(RandomAlphaModel())


class RandomAlphaModel(AlphaModel):
    def update(self, algorithm: QCAlgorithm, data: Slice) -> list[Insight]:
        insights = []

        for symbol in data.keys():  # type: ignore[reportCallIssue]
            direction = self._choice_random_direction()
            insight = Insight.price(symbol, timedelta(days=5), direction)
            insights.append(insight)

        self._log_insights(algorithm, insights)

        return insights

    def _choice_random_direction(self) -> InsightDirection:
        direction = random.choices(
            [InsightDirection.UP, InsightDirection.DOWN, InsightDirection.FLAT],
            weights=[0.5, 0.5, 0],
        )[0]

        return direction

    def _log_insights(self, algorithm: QCAlgorithm, insights: list[Insight]) -> None:
        algorithm.debug(f"{algorithm.time}: === Insights ===")
        for insight in insights:
            algorithm.debug(
                f"Symbol: {insight.symbol}, "
                f"Direction: {insight.direction}, "
                f"Duration: {insight.period}, "
            )
