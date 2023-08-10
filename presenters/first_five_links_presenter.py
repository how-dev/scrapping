from typing import List, AnyStr, Dict


class FirstFiveLinksPresenter:
    def __init__(self, links: List[AnyStr]):
        self.links = links

    def present(self) -> Dict:
        first_five_links = self.links[:5]
        return {
            "links": first_five_links,
        }
