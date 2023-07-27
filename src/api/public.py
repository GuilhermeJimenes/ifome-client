from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from src.presentation.payloads.buy import buy_ns
from src.presentation.payloads.user import user_ns
from src.presentation.resources.buy import Buy
from src.presentation.resources.user import Users, User

print('public')

# configs
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

# namespaces
api.add_namespace(user_ns)
api.add_namespace(buy_ns)

# resources
user_ns.add_resource(Users, '')
user_ns.add_resource(User, '/<string:_id>')
buy_ns.add_resource(Buy, '/<string:_id>')
