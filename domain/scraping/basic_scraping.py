from typing import List, Optional

import aiohttp
from bs4 import BeautifulSoup


class BasicScraping:
    def __init__(self,
                 scraping_url: str,
                 link_selector: dict,
                 scraping_headers: Optional[dict] = None):
        self.scraping_url = scraping_url
        self.link_selector = link_selector
        self.scraping_headers = scraping_headers or {}

    def get_links_by_html(self, html) -> List[str]:
        soup = BeautifulSoup(html, "html.parser")
        links: List[str] = []
        for result in soup.find_all(**self.link_selector):
            link = result.find("a", href=True)
            is_https = link and link["href"].startswith("https://")

            if is_https:
                links.append(link["href"])

        return links

    async def get_html(self, keyword: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.scraping_url}{keyword}", headers=self.scraping_headers
            ) as response:
                html = await response.text()
                return html

    async def get_links(self, keyword: str) -> List[str]:
        html = await self.get_html(keyword)
        return self.get_links_by_html(html)
