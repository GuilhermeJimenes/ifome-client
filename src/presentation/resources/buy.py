from flask import request
from flask_restx import Resource

from src.application.buy_app import BuyApp
from src.presentation.payloads.buy import buy_ns, buy_payload


class Buy(Resource):
    def get(self, _id):
        response = BuyApp().get_buy_by_id(_id)
        return response

    @buy_ns.expect(buy_payload, validate=True)
    def post(self, _id):
        data = request.get_json()

        response = BuyApp().create_buy(_id, data['food_name'])
        return response
