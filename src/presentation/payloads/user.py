from flask_restx import Namespace, fields

# Namespaces
user_ns = Namespace('user')

# Payloads
create_client_payload = user_ns.model('CreateClientPayload', {
    'name': fields.String(required=True),
    'email': fields.String(required=True),
    'address': fields.String(required=True)
}, strict=True)

# Headers
