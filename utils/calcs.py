import time

SEARCH_QUERIES = []


def calc_metrics_by_search_queries() -> dict:
    search_amount = len(SEARCH_QUERIES)
    queries = []
    average_time = 0

    if search_amount:
        total_time = 0
        for query in SEARCH_QUERIES:
            total_time += query["time"]
            queries.append(query["query"])

        average_time = total_time / search_amount

    return {"average_response_time": average_time, "search_queries": queries}


def register_query(func):
    def wrapper(*args, **kwargs):
        instance = args[0]

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time

        SEARCH_QUERIES.append({
            "query": instance.keyword, "time": execution_time
        })
        return result

    return wrapper
