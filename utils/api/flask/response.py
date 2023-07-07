from flask import jsonify

from utils.api.basic_response import BasicResponse


class FlaskResponse(BasicResponse):
    def success(self, response):
        return jsonify(response), 200

    def bad_request(self, error):
        return jsonify(error), 400
