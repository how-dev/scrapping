import time
from dataclasses import dataclass
from typing import List

from domain.scraping.basic.basic_web_scraping import WebClients


@dataclass
class SearchQuery:
    keyword: str
    client: WebClients
    execution_time: float


Queries = List[SearchQuery]
SEARCH_QUERIES: Queries = []


def register_query(search_queries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            instance = args[0]

            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            execution_time = end_time - start_time
            search_query = SearchQuery(
                keyword=instance.keyword,
                client=instance.client,
                execution_time=execution_time,
            )

            search_queries.append(search_query)
            return result

        return wrapper

    return decorator
