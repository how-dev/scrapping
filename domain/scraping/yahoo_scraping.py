from .basic_web_scraping import BasicWebScraping


class YahooScraping(BasicWebScraping):
    def __init__(self):
        super().__init__(scraping_url="https://search.yahoo.com/search?p=")
