from typing import AnyStr

from domain.controllers.get_links_controller import GetLinksController
from domain.scraping.basic.basic_web_scraping import (
    BasicWebScraping,
    WebClients
)
from interactors.calc_metrics_interactor import SEARCH_QUERIES
from utils.decorators import register_query


class WebScrapingInteractor:
    def __init__(
        self,
        keyword: AnyStr,
        web_scraping: BasicWebScraping,
        client: WebClients
    ):
        self.keyword = keyword
        self.web_scraping = web_scraping
        self.client = client

    @register_query(SEARCH_QUERIES)
    async def run(self):
        document = await self.web_scraping.get_document(self.keyword)
        print(document)
        controller = GetLinksController(document, self.client)

        links = controller.get_links()
        return links
