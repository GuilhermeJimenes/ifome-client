from flask_restx import Namespace, fields

# Namespaces
client_ns = Namespace('user')

# Payloads
create_client_payload = client_ns.model('CreateClientPayload', {
    'name': fields.String(required=True),
    'email': fields.String(required=True),
    'address': fields.String(required=True)
}, strict=True)

# Headers
