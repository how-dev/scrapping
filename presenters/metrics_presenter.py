from typing import Dict

from interactors.calc_metrics_interactor import CalcMetricsResponse


class MetricsPresenter:
    def __init__(self, metrics: CalcMetricsResponse):
        self.metrics = metrics

    def present(self) -> Dict:
        return {
            "average_response_time": self.metrics.average_response_time,
            "search_queries": self.metrics.search_queries,
        }
