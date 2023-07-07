from abc import ABC, abstractmethod


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
