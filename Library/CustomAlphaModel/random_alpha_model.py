from AlgorithmImports import *
from datetime import timedelta
import random


class RandomAlphaModel(AlphaModel):
    def __init__(self, period: int = 5, log_insights=False) -> None:
        self.period = timedelta(days=period)
        self.log_insights = log_insights

    def update(self, algorithm: QCAlgorithm, data: Slice) -> list[Insight]:
        insights = []

        for symbol in data.keys():
            active_insights = algorithm.insights.get_insights(
                lambda i: i.symbol == symbol and i.is_active(algorithm.utc_time)
            )

            if active_insights:
                continue

            direction = self._select_random_direction()
            insight = Insight.price(symbol, self.period, direction)
            insights.append(insight)

        if self.log_insights:
            self._log_insights(algorithm, insights)

        return insights

    def _select_random_direction(self) -> InsightDirection:
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
