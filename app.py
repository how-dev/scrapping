from flask import Flask

from domain.scraping.basic_web_scraping import WebClients
from interactors.web_scraping_interactor import WebScrapingInteractor

from presenters.first_five_links_presenter import FirstFiveLinksPresenter
from utils.decorators import require_query_param
from utils.api.flask.request import FlaskRequest
from utils.api.flask.response import FlaskResponse
from utils.getters import ScrapingFactory
from utils.calcs import calc_metrics_by_client

app = Flask(__name__)


@app.route("/metrics")
@require_query_param(
    response_cls=FlaskResponse,
    request_cls=FlaskRequest,
    query_param_name="client",
    enum=WebClients
)
async def metrics(client: WebClients):
    api_response = FlaskResponse()
    calculated_search_metrics = calc_metrics_by_client(client)

    return api_response.success(calculated_search_metrics)


@app.route("/search")
@require_query_param(
    response_cls=FlaskResponse,
    request_cls=FlaskRequest,
    query_param_name="keyword"
)
@require_query_param(
    response_cls=FlaskResponse,
    request_cls=FlaskRequest,
    query_param_name="client",
    enum=WebClients,
)
async def search(keyword: str, client: WebClients):
    api_response = FlaskResponse()
    scraping = ScrapingFactory(client).scraping
    interactor = WebScrapingInteractor(keyword, scraping, client)

    links = await interactor.run()
    presenter = FirstFiveLinksPresenter(links)
    response = presenter.present()

    return api_response.success(response)
