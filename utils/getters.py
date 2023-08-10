from domain.scraping import BingScraping, GoogleScraping
from domain.scraping.basic_web_scraping import WebClients
from domain.scraping.yahoo_scraping import YahooScraping


class GetScrapingError(Exception):
    pass


class ScrapingFactory:
    CLIENTS = {
        WebClients.GOOGLE: GoogleScraping,
        WebClients.BING: BingScraping,
        WebClients.YAHOO: YahooScraping,
    }

    def __init__(self, client: WebClients):
        self.client = client

    @property
    def scraping(self):
        try:
            return self.CLIENTS[self.client]()
        except KeyError:
            raise GetScrapingError("Client not found")
