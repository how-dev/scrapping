from .basic_scraping import BasicScraping


class GoogleScraping(BasicScraping):
    def __init__(self):
        super().__init__(
            scraping_url="https://www.google.com/search?q=",
            link_selector={"name": "div", "class_": "g"},
            scraping_headers={
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
                )
            },
        )
