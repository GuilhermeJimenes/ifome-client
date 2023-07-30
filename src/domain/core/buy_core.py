from src.domain.interfaces.deliveries_interface import BuyMessageBroker, DeliveriesStorage
from src.domain.interfaces.client_interface import ClientStorage
from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.domain.models.delivery_model import DeliveryModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.utils.parser import create_hash


class GetBuyById:
    def __init__(self, deliveries_storage: DeliveriesStorage):
        self.deliveries_storage = deliveries_storage

    def get_buy_by_id(self, delivery_id):
        return self.deliveries_storage.get_by_id(delivery_id)


class CreateBuyCore:
    def __init__(self, client_storage: ClientStorage, deliveries_storage: DeliveriesStorage,
                 deliveryman_storage: DeliverymanStorage, buy_message_broker: BuyMessageBroker):
        self.client_storage = client_storage
        self.deliveries_storage = deliveries_storage
        self.deliveryman_storage = deliveryman_storage
        self.buy_message_broker = buy_message_broker

    def check_available(self):
        if deliveryman_id := self.deliveryman_storage.get_available():
            if deliveryman_id := deliveryman_id[0]:
                return deliveryman_id
        raise NotFoundFail('Deliveryman not found')

    def get_address(self, client_id):
        return self.client_storage.get_by_id(client_id, 'address')[0]

    def new_delivery(self, client_id, address, food_name):
        delivery_id = create_hash()
        delivery = DeliveryModel(delivery_id, client_id, food_name, address)
        self.deliveries_storage.save(delivery)
        return delivery

    def send_delivery(self, delivery_id):
        self.buy_message_broker.publish_buy(delivery_id)
        self.buy_message_broker.close_connection()

    def create_buy(self, client_id, food_name):
        self.check_available()
        address = self.get_address(client_id)
        delivery = self.new_delivery(client_id, address, food_name)
        self.send_delivery(delivery.delivery_id)
        return delivery
