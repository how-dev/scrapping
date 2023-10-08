from typing import AnyStr

from flask import Flask

from domain.scraping.basic.basic_web_scraping import WebClients
from interactors.calc_metrics_interactor import CalcMetricsInteractor
from interactors.web_scraping_interactor import WebScrapingInteractor

from presenters.first_five_links_presenter import FirstFiveLinksPresenter
from presenters.metrics_presenter import MetricsPresenter
from utils.decorators import require_query_param
from utils.api.flask.request import FlaskRequest
from utils.api.flask.response import FlaskResponse
from utils.getters import ScrapingFactory

app = Flask(__name__)


def get_scraping(client: WebClients):
    factory = ScrapingFactory(client)
    scraping = factory.get_scraping()
    return scraping


@app.route("/metrics")
@require_query_param(
    response_cls=FlaskResponse,
    request_cls=FlaskRequest,
    query_param_name="client",
    enum=WebClients,
)
async def metrics(client: WebClients):
    api_response = FlaskResponse()
    interactor = CalcMetricsInteractor(client)
    calculated_metrics = interactor.run()

    presenter = MetricsPresenter(calculated_metrics)
    response = presenter.present()

    return api_response.success(response)


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
    default_value=WebClients.GOOGLE.value,
    enum=WebClients,
)
async def search(keyword: AnyStr, client: WebClients):
    api_response = FlaskResponse()
    scraping = get_scraping(client)
    interactor = WebScrapingInteractor(keyword, scraping, client)

    links = await interactor.run()
    presenter = FirstFiveLinksPresenter(links)
    response = presenter.present()

    return api_response.success(response)
