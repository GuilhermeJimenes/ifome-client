from flask import request
from flask_restx import Resource

from src.application.user_app import UserApp
from src.presentation.payloads.user import user_ns, create_client_payload


class Users(Resource):
    def get(self):
        response = UserApp().get_all_users()
        return response

    @user_ns.expect(create_client_payload, validate=True)
    def post(self):
        data = request.get_json()

        response = UserApp().create_user(data['name'], data['email'], data['address'])
        return response


class User(Resource):
    def get(self, _id):
        response = UserApp().get_user_by_id(_id)
        return response
