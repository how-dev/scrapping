from config import Clients
from domain.scraping import BingScraping, GoogleScraping
from domain.scraping.yahoo_scraping import YahooScraping


class GetScrapingError(Exception):
    pass


class ScrapingFactory:
    CLIENTS = {
        Clients.GOOGLE: GoogleScraping,
        Clients.BING: BingScraping,
        Clients.YAHOO: YahooScraping,
    }

    def __init__(self, client: Clients):
        self.client = client

    @property
    def scraping(self):
        try:
            return self.CLIENTS[self.client]()
        except KeyError:
            raise GetScrapingError("Client not found")
