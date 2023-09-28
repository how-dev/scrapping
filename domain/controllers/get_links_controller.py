from typing import AnyStr, List

from bs4 import BeautifulSoup

from domain.scraping.basic.basic_web_scraping import WebClients


class GetLinksController:
    LINKS_SELECTOR = {
        WebClients.GOOGLE: {"name": "div", "class_": "g"},
        WebClients.BING: {"name": "li", "class": "b_algo"},
        WebClients.YAHOO: {"name": "div", "class_": "algo-sr"},
    }

    def __init__(self, html: AnyStr, client: WebClients):
        self.html = html
        self.client = client

    def get_links(self) -> List[AnyStr]:
        soup = BeautifulSoup(self.html, "html.parser")
        links: List[AnyStr] = []
        for result in soup.find_all(**self.LINKS_SELECTOR[self.client]):
            link = result.find("a", href=True)
            is_https = link and link["href"].startswith("https://")

            if is_https:
                links.append(link["href"])

        return links
