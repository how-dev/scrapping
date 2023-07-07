from abc import ABC, abstractmethod


class BasicRequest(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_body(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_query_params(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_headers(self) -> dict:
        raise NotImplementedError
