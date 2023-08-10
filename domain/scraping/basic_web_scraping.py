from enum import Enum
from typing import Optional, Dict, AnyStr

import aiohttp

from domain.scraping.basic_scraping import BasicScraping


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

        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{url}{keyword}", headers=headers
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
