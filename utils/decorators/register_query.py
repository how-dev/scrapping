import time


def register_query(search_queries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            instance = args[0]

            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            execution_time = end_time - start_time

            search_queries.append({
                "query": instance.keyword, "time": execution_time
            })
            return result

        return wrapper

    return decorator
