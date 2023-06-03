from abc import ABC, abstractmethod
from typing import List, Optional

from bs4 import BeautifulSoup


class BasicScraping(ABC):
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

    @abstractmethod
    async def get_html(self, keyword: str) -> str:
        raise NotImplementedError  # pragma: no cover

    async def get_links(self, keyword: str) -> List[str]:
        html = await self.get_html(keyword)
        return self.get_links_by_html(html)
