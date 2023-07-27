from flask_restx import Namespace, fields

# Namespaces
buy_ns = Namespace('buy')

# Payloads
buy_payload = buy_ns.model('BuyPayload', {
    'food_name': fields.String(required=True)
}, strict=True)

# Headers
