from abc import ABC, abstractmethod
from functools import wraps

from flask import request


def require_query_param(response_cls, query_param_name):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            query_param = request.args.get(query_param_name)
            if not query_param:
                response = response_cls()
                return response.bad_request({
                    "error": f"Query parameter '{query_param_name}' not found"
                })

            kwargs[query_param_name] = query_param
            return await func(*args, **kwargs)

        return wrapper

    return decorator


class BasicResponse(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def success(self, response):
        raise NotImplementedError

    @abstractmethod
    def bad_request(self, error):
        raise NotImplementedError

    # And others like no_content, not_found, etc............
