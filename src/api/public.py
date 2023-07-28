from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from src.presentation.payloads.buy import buy_ns
from src.presentation.payloads.user import client_ns
from src.presentation.resources.buy import Buy
from src.presentation.resources.client import Clients, Client

print('public')

# configs
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

# namespaces
api.add_namespace(client_ns)
api.add_namespace(buy_ns)

# resources
client_ns.add_resource(Clients, '')
client_ns.add_resource(Client, '/<string:_id>')
buy_ns.add_resource(Buy, '/<string:_id>')
