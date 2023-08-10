from typing import List

from domain.scraping.basic_web_scraping import WebClients
from utils.decorators.register_query import SearchQuery

SEARCH_QUERIES: List[SearchQuery] = []


def calc_metrics_by_client(client: WebClients) -> dict:
    search_query_by_client = list(
        filter(lambda q: q.client == client, SEARCH_QUERIES)
    )
    search_amount = len(search_query_by_client)
    queries = []
    average_time = 0

    if search_amount:
        total_time = 0
        for query in search_query_by_client:
            total_time += query.execution_time
            queries.append(query.keyword)

        average_time = total_time / search_amount

    return {"average_response_time": average_time, "search_queries": queries}
