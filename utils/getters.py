from domain.scraping import (
    BingScraping,
    GoogleScraping
)
from domain.scraping.yahoo_scraping import YahooScraping


def get_google_scraping() -> GoogleScraping:
    return GoogleScraping()


def get_bing_scraping() -> BingScraping:
    return BingScraping()


def get_yahoo_scraping() -> YahooScraping:
    return YahooScraping()
