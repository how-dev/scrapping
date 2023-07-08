from abc import ABC, abstractmethod

from domain.scraping.basic_scraping import BasicScraping
from utils.calcs import BING_SEARCH_QUERIES, GOOGLE_SEARCH_QUERIES, \
    YAHOO_SEARCH_QUERIES
from utils.decorators import register_query


class BasicScrapingInteractor(ABC):
    def __init__(self, keyword: str, scraping: BasicScraping):
        self.keyword = keyword
        self.scraping = scraping

    @abstractmethod
    async def run(self):
        links = await self.scraping.get_links(self.keyword)
        return links


class BingScrapingInteractor(BasicScrapingInteractor):
    @register_query(BING_SEARCH_QUERIES)
    async def run(self):
        return await super().run()


class GoogleScrapingInteractor(BasicScrapingInteractor):
    @register_query(GOOGLE_SEARCH_QUERIES)
    async def run(self):
        return await super().run()


class YahooScrapingInteractor(BasicScrapingInteractor):
    @register_query(YAHOO_SEARCH_QUERIES)
    async def run(self):
        return await super().run()
