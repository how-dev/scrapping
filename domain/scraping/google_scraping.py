from typing import Optional

import aiohttp

from .basic_scraping import BasicScraping


class GoogleScraping(BasicScraping):
    def __init__(
        self,
        scraping_url: Optional[str] = "https://www.google.com/search?q=",
        scraping_headers: Optional[dict] = None,
    ):
        super().__init__(
            scraping_url=scraping_url,
            scraping_headers=scraping_headers
            or {
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
                )
            },
        )

    async def get_html(self, keyword: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.scraping_url}{keyword}", headers=self.scraping_headers
            ) as response:
                html = await response.text()
                return html
