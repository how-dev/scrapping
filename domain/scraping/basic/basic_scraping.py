from abc import ABC, abstractmethod
from typing import AnyStr


class BasicScraping(ABC):
    @abstractmethod
    async def get_document(self, keyword: AnyStr) -> AnyStr:
        raise NotImplementedError  # pragma: no cover
