from typing import AnyStr

from domain.scraping.basic.basic_web_scraping import BasicWebScraping


class YahooScraping(BasicWebScraping):
    def __init__(self):
        super().__init__(scraping_url=(
            "https://search.yahoo.com/search;"
            "_ylt=AwrNZsuLCthk2SEmuxjy6Qt.;"
            "_ylc=X1MDMjExNDcxMDAwMgRfcgMyBGZyAwRmcjIDcDpzLHY6c2ZwLG06c2Esc2Ff"
            "bWs6MTMEZ3ByaWQDMXFTZ2x0NkhUakM4dW9jVDh1Ty5VQQRuX3JzbHQDMARuX3N1Z"
            "2cDMQRvcmlnaW4DYnIuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMQRwcXN0cgMEcHFzdH"
            "JsAzAEcXN0cmwDNgRxdWVyeQNob3dhcmQEdF9zdG1wAzE2OTE4ODAwODQEdXNlX2N"
            "hc2UD?p="
        ))

    @staticmethod
    def clean_keyword(keyword: AnyStr) -> AnyStr:
        return (
            f"{keyword}"
            f"&fr=sfp"
            f"&fr2=p%3As%2Cv%3Asfp%2Cm%3Asa%2Csa_mk%3A13"
            f"&iscqry="
            f"&mkr=13"
        )
