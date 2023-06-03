class GoogleScrapingPresenter:
    def __init__(self, links: list):
        self.links = links

    def present(self) -> dict:
        first_five_links = self.links[:5]
        return {
            "links": first_five_links,
        }
