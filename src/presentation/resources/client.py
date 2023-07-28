from flask import request
from flask_restx import Resource

from src.application.client_app import ClientApp
from src.presentation.payloads.user import client_ns, create_client_payload


class Clients(Resource):
    def get(self):
        response = ClientApp().get_all_clients()
        return response

    @client_ns.expect(create_client_payload, validate=True)
    def post(self):
        data = request.get_json()

        response = ClientApp().create_client(data['name'], data['email'], data['address'])
        return response


class Client(Resource):
    def get(self, _id):
        response = ClientApp().get_client_by_id(_id)
        return response
