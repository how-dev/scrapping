from flask import Flask

from interactors.google_scraping import GoogleScrapingInteractor
from presenters.google_scraping import GoogleScrapingPresenter
from utils.basic_response import require_query_param
from utils.flask.response import FlaskResponse
from utils.getters import get_google_scraping
from utils.calcs import calc_metrics_by_search_queries

app = Flask(__name__)


@app.route("/metrics")
def metrics():
    api_response = FlaskResponse()
    calculated_search_metrics = calc_metrics_by_search_queries()

    return api_response.success(calculated_search_metrics)


@app.route("/search")
@require_query_param(FlaskResponse, "keyword")
async def google_search(keyword: str):
    api_response = FlaskResponse()

    google_scraping = get_google_scraping()
    interactor = GoogleScrapingInteractor(keyword, google_scraping)

    links = await interactor.run()
    presenter = GoogleScrapingPresenter(links)

    return api_response.success(presenter.present())
