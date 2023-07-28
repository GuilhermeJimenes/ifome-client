from src.api.http.http_response import HttpResponse
from src.domain.constants import STORAGE_TYPE, MESSAGE_BROKER_TYPE
from src.domain.core.buy_core import CreateBuyCore, GetBuyById
from src.domain.interfaces.deliveries_interface import BuyMessageBroker, DeliveriesStorage
from src.domain.interfaces.client_interface import ClientStorage
from src.exceptions.custom_exceptions import RabbitMQError, NotFoundFail
from src.infrastructure.buy_message_broker_rabbitmq import BuyMessageBrokerRabbitMQ
from src.infrastructure.deliveries_storage_mysql import DeliveriesStorageMySQL
from src.infrastructure.deliveries_storage_sqlite import DeliveriesStorageSQLite
from src.infrastructure.clients_storage_mysql import ClientsStorageMySQL
from src.infrastructure.clients_storage_sqlite import ClientsStorageSQLite


class BuyApp:
    def __init__(self):
        if STORAGE_TYPE == "mysql":
            self.user_storage: ClientStorage = ClientsStorageMySQL()
            self.deliveries_storage: DeliveriesStorage = DeliveriesStorageMySQL()
        elif STORAGE_TYPE == "sqlite":
            self.user_storage: ClientStorage = ClientsStorageSQLite()
            self.deliveries_storage: DeliveriesStorage = DeliveriesStorageSQLite()
        else:
            raise ValueError("Invalid storage, valid types: sqlite, mysql")

        if MESSAGE_BROKER_TYPE == "rabbitmq":
            self.buy_message_broker: BuyMessageBroker = BuyMessageBrokerRabbitMQ()
        else:
            raise ValueError("Invalid message broker, valid types: rabbitmq")

    def get_buy_by_id(self, delivery_id):
        try:
            buy_core = GetBuyById(self.deliveries_storage)
            response = buy_core.get_buy_by_id(delivery_id)
            return HttpResponse.success('Successfully found buy!', response.__dict__)
        except NotFoundFail as error:
            return HttpResponse.internal_error(message=str(error))

    def create_buy(self, client_id, food_name):
        try:
            buy_core = CreateBuyCore(self.user_storage, self.deliveries_storage, self.buy_message_broker)
            response = buy_core.create_buy(client_id, food_name)
            return HttpResponse.success('Successfully registered buy!', response.__dict__)
        except RabbitMQError as error:
            return HttpResponse.internal_error(message=str(error))
