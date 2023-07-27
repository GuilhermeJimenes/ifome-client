import json

from src.domain.interfaces.buy_interface import BuyMessageBroker, BuyStorage
from src.domain.interfaces.user_interface import UserStorage
from src.domain.models.delivery_model import DeliveryModel
from src.utils.parser import create_hash


class GetBuyById:
    def __init__(self, buy_storage: BuyStorage):
        self.buy_storage = buy_storage

    def get_buy_by_id(self, delivery_id):
        return self.buy_storage.get_by_id(delivery_id)


class CreateBuyCore:
    def __init__(self, user_storage: UserStorage, buy_storage: BuyStorage, buy_message_broker: BuyMessageBroker):
        self.user_storage = user_storage
        self.buy_storage = buy_storage
        self.buy_message_broker = buy_message_broker

    def get_address(self, client_id):
        return self.user_storage.get_by_id(client_id, 'address')[0]

    def new_delivery(self, client_id, food_name):
        delivery_id = create_hash()
        address = self.get_address(client_id)
        delivery = DeliveryModel(delivery_id, client_id, food_name, address)
        self.buy_storage.save(delivery)
        return delivery

    def send_delivery(self, delivery_id, food_name):
        message = json.dumps({delivery_id: food_name})
        self.buy_message_broker.send_buy(message)
        self.buy_message_broker.connection_close()

    def create_buy(self, client_id, food_name):
        delivery = self.new_delivery(client_id, food_name)
        self.send_delivery(str(delivery.delivery_id), food_name)
        return delivery
