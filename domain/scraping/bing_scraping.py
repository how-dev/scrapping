from domain.scraping.basic.basic_web_scraping import BasicWebScraping


class BingScraping(BasicWebScraping):
    def __init__(self):
        super().__init__(scraping_url="https://www.bing.com/search?q=")
