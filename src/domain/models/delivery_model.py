from dataclasses import dataclass


@dataclass
class DeliveryModel:
    delivery_id: str
    client_id: str
    food_name: str
    address: str
    deliveryman_id: str = ""
    status: str = ""
