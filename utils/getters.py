from domain.scraping import BingScraping, GoogleScraping
from domain.scraping.basic.basic_web_scraping import WebClients
from domain.scraping.yahoo_scraping import YahooScraping


class GetScrapingError(ValueError):
    pass


class ScrapingFactory:
    CLIENTS = {
        WebClients.GOOGLE: GoogleScraping,
        WebClients.BING: BingScraping,
        WebClients.YAHOO: YahooScraping,
    }

    def __init__(self, client: WebClients):
        self.client = client

    def get_scraping(self):
        is_valid_client = self.client in self.CLIENTS

        if not is_valid_client:
            raise GetScrapingError("Client not found")

        current_client = self.CLIENTS[self.client]
        return current_client()
