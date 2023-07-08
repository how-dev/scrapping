GOOGLE_SEARCH_QUERIES = []
BING_SEARCH_QUERIES = []
YAHOO_SEARCH_QUERIES = []


def calc_metrics_by_client(client: str) -> dict:
    search_queries = _get_search_queries(client)
    search_amount = len(search_queries)
    queries = []
    average_time = 0

    if search_amount:
        total_time = 0
        for query in search_queries:
            total_time += query["time"]
            queries.append(query["query"])

        average_time = total_time / search_amount

    return {"average_response_time": average_time, "search_queries": queries}


def _get_search_queries(client: str):
    client_search_queries = {
        "google": GOOGLE_SEARCH_QUERIES,
        "bing": BING_SEARCH_QUERIES,
        "yahoo": YAHOO_SEARCH_QUERIES,
    }
    search_queries = client_search_queries.get(client, [])
    return search_queries
