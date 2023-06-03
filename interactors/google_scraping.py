from domain.scraping.google_scraping import GoogleScraping
from utils.calcs import register_query


class GoogleScrapingInteractor:
    def __init__(self, keyword: str, scraping: GoogleScraping):
        self.keyword = keyword
        self.scraping = scraping

    @register_query
    async def run(self):
        links = await self.scraping.get_links(self.keyword)
        return links
