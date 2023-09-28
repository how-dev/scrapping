from domain.scraping.basic.basic_web_scraping import BasicWebScraping


class GoogleScraping(BasicWebScraping):
    def __init__(self):
        super().__init__(scraping_url="https://www.google.com/search?q=")
