from enum import Enum
from functools import wraps
from typing import Type, Optional, AnyStr, Any

from utils.api.basic_request import BasicRequest
from utils.api.basic_response import BasicResponse


def require_query_param(
    response_cls: Type[BasicResponse],
    request_cls: Type[BasicRequest],
    query_param_name: AnyStr,
    default_value: Optional[Any] = None,
    enum: Optional[Type[Enum]] = None,
):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = request_cls()
            query_params = request.get_query_params()
            query_param = query_params.get(query_param_name, default_value)
            if not query_param:
                response = response_cls()
                return response.bad_request(
                    {
                        "error": (
                            f"Query parameter '{query_param_name}' not found"
                        )
                    }
                )

            if enum:
                option_values = [option.value for option in enum]
                if query_param not in option_values:
                    response = response_cls()
                    return response.bad_request(
                        {
                            "error": (
                                f"Query parameter '{query_param_name}' "
                                f"must be one of {option_values}"
                            )
                        }
                    )
                else:
                    query_param = enum(query_param)

            kwargs[query_param_name] = query_param
            return await func(*args, **kwargs)

        return wrapper

    return decorator
