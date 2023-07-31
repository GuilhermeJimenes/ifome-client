from flask_restx import Namespace, fields

# Namespaces
client_ns = Namespace("client")

# Payloads
create_client_payload = client_ns.model("CreateClientPayload", {
    "name": fields.String(required=True, example="GuilhermeMJ"),
    "email": fields.String(required=True, example="gui@gmail.com"),
    "address": fields.String(required=True, example='rua machado 123')
}, strict=True)

# Headers
