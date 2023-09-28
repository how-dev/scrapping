import logging
from enum import Enum
from typing import Optional, Dict, AnyStr

import aiohttp

from domain.scraping.basic.basic_scraping import BasicScraping

logger = logging.getLogger(__name__)


class WebClients(Enum):
    GOOGLE = "google"
    BING = "bing"
    YAHOO = "yahoo"


class BasicWebScraping(BasicScraping):
    def __init__(
        self,
        scraping_url: AnyStr,
        scraping_headers: Optional[Dict] = None,
    ):
        self.scraping_url = scraping_url
        self.scraping_headers = scraping_headers or {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
            )
        }

    async def get_document(self, keyword: AnyStr) -> AnyStr:
        return await self._get_html(keyword)

    async def _get_html(self, keyword: AnyStr) -> AnyStr:
        headers = self.get_scraping_headers()
        url = self.get_scraping_url()
        keyword = self.clean_keyword(keyword)

        full_url = f"{url}{keyword}"

        async with aiohttp.ClientSession() as session:
            async with session.get(
                full_url, headers=headers
            ) as response:
                html = await response.text()
                return html

    def get_scraping_headers(self) -> Dict:
        """
        Override this method to manipulate the headers before the request
        :return: Dict
        """
        return self.scraping_headers

    def get_scraping_url(self) -> AnyStr:
        """
        Override this method to manipulate the url before the request
        :return: AnyStr
        """
        return self.scraping_url

    @staticmethod
    def clean_keyword(keyword: AnyStr) -> AnyStr:
        """
        Override this method to manipulate the keyword before the request
        :param keyword: AnyStr
        :return: AnyStr
        """
        return keyword

    def __repr__(self):
        return f"{self.__class__.__name__}({self.scraping_url})"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if not isinstance(other, BasicWebScraping):
            return False

        return (
            self.scraping_url == other.scraping_url and
            self.scraping_headers == other.scraping_headers
        )

    def __hash__(self):
        return hash((self.scraping_url, self.scraping_headers))

    def __ne__(self, other):
        return not self.__eq__(other)
