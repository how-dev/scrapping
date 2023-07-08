from flask import Flask

from interactors.scraping_interactor import (
    BingScrapingInteractor,
    GoogleScrapingInteractor, YahooScrapingInteractor
)

from presenters.first_five_links_presenter import FirstFiveLinksPresenter
from utils.decorators import require_query_param
from utils.api.flask.request import FlaskRequest
from utils.api.flask.response import FlaskResponse
from utils.getters import (
    get_google_scraping,
    get_bing_scraping,
    get_yahoo_scraping
)
from utils.calcs import calc_metrics_by_client

app = Flask(__name__)


@app.route("/metrics")
@require_query_param(
    response_cls=FlaskResponse,
    request_cls=FlaskRequest,
    query_param_name="client"
)
async def metrics(client: str):
    api_response = FlaskResponse()
    calculated_search_metrics = calc_metrics_by_client(client)

    return api_response.success(calculated_search_metrics)


@app.route("/google-search")
@require_query_param(
    response_cls=FlaskResponse,
    request_cls=FlaskRequest,
    query_param_name="keyword"
)
async def google_search(keyword: str):
    api_response = FlaskResponse()

    google_scraping = get_google_scraping()
    interactor = GoogleScrapingInteractor(keyword, google_scraping)

    links = await interactor.run()
    presenter = FirstFiveLinksPresenter(links)
    response = presenter.present()

    return api_response.success(response)


@app.route("/bing-search")
@require_query_param(
    response_cls=FlaskResponse,
    request_cls=FlaskRequest,
    query_param_name="keyword"
)
async def bing_search(keyword: str):
    api_response = FlaskResponse()

    bing_scraping = get_bing_scraping()
    interactor = BingScrapingInteractor(keyword, bing_scraping)

    links = await interactor.run()
    presenter = FirstFiveLinksPresenter(links)
    response = presenter.present()

    return api_response.success(response)


@app.route("/yahoo-search")
@require_query_param(
    response_cls=FlaskResponse,
    request_cls=FlaskRequest,
    query_param_name="keyword"
)
async def yahoo_search(keyword: str):
    api_response = FlaskResponse()

    bing_scraping = get_yahoo_scraping()
    interactor = YahooScrapingInteractor(keyword, bing_scraping)

    links = await interactor.run()
    presenter = FirstFiveLinksPresenter(links)
    response = presenter.present()

    return api_response.success(response)
