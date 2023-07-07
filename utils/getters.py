from domain.scraping import (
    BingScraping,
    GoogleScraping
)


def get_google_scraping() -> GoogleScraping:
    return GoogleScraping()


def get_bing_scraping() -> BingScraping:
    return BingScraping()
