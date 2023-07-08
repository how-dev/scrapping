from .basic_scraping import BasicScraping


class YahooScraping(BasicScraping):
    def __init__(self):
        super().__init__(
            scraping_url="https://search.yahoo.com/search?p=",
            link_selector={"name": "div", "class_": "algo-sr"},
            scraping_headers={
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
                )
            },
        )
