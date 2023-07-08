from config import Clients
from domain.scraping.basic_scraping import BasicScraping
from utils.calcs import SEARCH_QUERIES
from utils.decorators import register_query


class ScrapingInteractor:
    def __init__(self, keyword: str, scraping: BasicScraping, client: Clients):
        self.keyword = keyword
        self.scraping = scraping
        self.client = client

    @register_query(SEARCH_QUERIES)
    async def run(self):
        links = await self.scraping.get_links(self.keyword)
        return links
