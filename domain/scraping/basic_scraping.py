from typing import List, Optional

import aiohttp
from bs4 import BeautifulSoup


class BasicScraping:
    def __init__(self,
                 scraping_url: str,
                 scraping_headers: Optional[dict] = None):
        self.scraping_url = scraping_url
        self.scraping_headers = scraping_headers or {}

    @staticmethod
    def get_links_by_html(html) -> List[str]:
        soup = BeautifulSoup(html, "html.parser")
        links: List[str] = []

        for result in soup.find_all("div", class_="g"):
            link = result.find("a", href=True)
            if link:
                links.append(link["href"])

        return links

    async def get_html(self, keyword: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{self.scraping_url}{keyword}",
                    headers=self.scraping_headers
            ) as response:
                html = await response.text()
                return html

    async def get_links(self, keyword: str) -> List[str]:
        html = await self.get_html(keyword)
        return self.get_links_by_html(html)
