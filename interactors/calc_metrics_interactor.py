from dataclasses import dataclass
from typing import AnyStr, List

from domain.scraping.basic.basic_web_scraping import WebClients
from utils.decorators.register_query import SearchQuery, SEARCH_QUERIES


@dataclass
class CalcMetricsResponse:
    average_response_time: float
    search_queries: List[AnyStr]


class CalcMetricsInteractor:
    def __init__(self, client: WebClients):
        self.client = client

    def run(self) -> CalcMetricsResponse:
        search_query_by_client = self._get_searches()
        queries = self._get_queries(search_query_by_client)
        average_time = self._get_average_time(search_query_by_client)

        return CalcMetricsResponse(
            average_response_time=average_time,
            search_queries=queries
        )

    @staticmethod
    def _get_queries(
        search_query_by_client: List[SearchQuery]
    ) -> List[AnyStr]:
        return [
            query.keyword for query in search_query_by_client
        ]

    def _get_average_time(
        self, search_query_by_client: List[SearchQuery]
    ) -> float:
        average_time = 0
        search_amount = len(search_query_by_client)
        if search_amount:
            total_time = self._get_total_time(search_query_by_client)

            average_time = total_time / search_amount
        return average_time

    @staticmethod
    def _get_total_time(search_query_by_client: List[SearchQuery]) -> float:
        return sum(
            [query.execution_time for query in search_query_by_client]
        )

    def _get_searches(self) -> List[SearchQuery]:
        return [
            query for query in SEARCH_QUERIES if query.client == self.client
        ]
