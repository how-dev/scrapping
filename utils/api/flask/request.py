from flask import request

from utils.api.basic_request import BasicRequest


class FlaskRequest(BasicRequest):
    def get_body(self) -> dict:
        return request.json

    def get_query_params(self) -> dict:
        return request.args

    def get_headers(self) -> dict:
        return request.headers
