from AlgorithmImports import *
from datetime import timedelta
import random


class RandomAlphaModel(AlphaModel):
    def __init__(self, period: int = 5) -> None:
        self.period = timedelta(days=period)

    def update(self, algorithm: QCAlgorithm, data: Slice) -> list[Insight]:
        insights = []

        active_symbols = {
            insight.symbol
            for insight in algorithm.insights.get_active_insights(algorithm.utc_time)  # type: ignore
        }

        for symbol in data.keys():
            if symbol.canonical != symbol:
                continue

            if symbol in active_symbols:
                continue

            direction = self._select_random_direction()
            insights.append(Insight.price(symbol, self.period, direction))

        return insights

    def _select_random_direction(self) -> InsightDirection:
        direction = random.choices(
            [InsightDirection.UP, InsightDirection.DOWN, InsightDirection.FLAT],
            weights=[0.5, 0.5, 0],
        )[0]

        return direction
