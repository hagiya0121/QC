from AlgorithmImports import *


class Logger:
    def __init__(self, algorithm: QCAlgorithm):
        self.algorithm = algorithm
        self._previous_canonicals = set()

    def log_if_canonical_changed(self) -> None:
        current = self._get_current_canonicals()

        if current != self._previous_canonicals:
            timestamp = self.algorithm.time.strftime("%Y-%m-%d(%a) %H:%M")
            self.algorithm.debug(f"{timestamp}: === Universe Selection ===")
            self.algorithm.debug(f"Count: {len(current)}")

            for symbol in sorted(current, key=lambda s: s.value):
                mapped = self.algorithm.active_securities[symbol].mapped
                self.algorithm.debug(f"Symbol: {symbol} Mapped: {mapped}")

            self._previous_canonicals = current

    def _get_current_canonicals(self) -> set[Symbol]:
        return {
            kvp.key  # type: ignore
            for kvp in self.algorithm.active_securities
            if kvp.key.is_canonical()
        }
