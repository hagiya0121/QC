from AlgorithmImports import *


class Logger:
    def __init__(self, algorithm: QCAlgorithm):
        self.algorithm = algorithm
        self._previous_canonicals = set()

    def log_if_canonical_changed(self) -> None:
        current = self._get_current_canonicals()

        if current != self._previous_canonicals:
            self.algorithm.debug(f"{self._timestamp()}: === Universe Selection ===")
            self.algorithm.debug(f"Count: {len(current)}")

            for symbol in sorted(current, key=lambda s: s.value):
                mapped = self.algorithm.active_securities[symbol].mapped
                self.algorithm.debug(f"Symbol: {symbol} Mapped: {mapped}")

            self._previous_canonicals = current

    def log_insights(self) -> None:
        active_insights = self.algorithm.insights.get_active_insights(
            self.algorithm.utc_time
        )

        if not active_insights:
            self.algorithm.debug(f"{self._timestamp()}: === No active insights ===")
            return

        self.algorithm.debug(f"{self._timestamp()}: === Insights ===")
        for insight in active_insights:
            self.algorithm.debug(
                f"Symbol: {insight.symbol}, Direction: {insight.direction}"
            )

    def _get_current_canonicals(self) -> set[Symbol]:
        return {
            kvp.key  # type: ignore
            for kvp in self.algorithm.active_securities
            if kvp.key.is_canonical()
        }

    def _timestamp(self) -> str:
        return self.algorithm.time.strftime("%Y-%m-%d(%a) %H:%M")
