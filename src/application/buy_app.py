from src.api.http.http_response import HttpResponse
from src.domain.constants import STORAGE_TYPE, MESSAGE_BROKER_TYPE
from src.domain.core.buy_core import CreateBuyCore, GetBuyById
from src.domain.interfaces.buy_interface import BuyMessageBroker, BuyStorage
from src.domain.interfaces.user_interface import UserStorage
from src.exceptions.custom_exceptions import RabbitMQError, NotFoundFail
from src.infrastructure.buy_message_broker_rabbitmq import BuyMessageBrokerRabbitMQ
from src.infrastructure.buy_storage_mysql import BuyStorageMySQL
from src.infrastructure.buy_storage_sqlite import BuyStorageSQLite
from src.infrastructure.user_storage_mysql import UserStorageMySQL
from src.infrastructure.user_storage_sqlite import UserStorageSQLite


class BuyApp:
    def __init__(self):
        if STORAGE_TYPE == "mysql":
            self.user_storage: UserStorage = UserStorageMySQL()
            self.buy_storage: BuyStorage = BuyStorageMySQL()
        elif STORAGE_TYPE == "sqlite":
            self.user_storage: UserStorage = UserStorageSQLite()
            self.buy_storage: BuyStorage = BuyStorageSQLite()
        else:
            raise ValueError("Invalid storage, valid types: sqlite, mysql")

        if MESSAGE_BROKER_TYPE == "rabbitmq":
            self.buy_message_broker: BuyMessageBroker = BuyMessageBrokerRabbitMQ()
        else:
            raise ValueError("Invalid message broker, valid types: rabbitmq")

    def get_buy_by_id(self, delivery_id):
        try:
            buy_use_cases = GetBuyById(self.buy_storage)
            response = buy_use_cases.get_buy_by_id(delivery_id)
            return HttpResponse.success('Successfully found buy!', response.__dict__)
        except NotFoundFail as error:
            return HttpResponse.internal_error(message=str(error))

    def create_buy(self, client_id, food_name):
        try:
            buy_use_cases = CreateBuyCore(self.user_storage, self.buy_storage, self.buy_message_broker)
            response = buy_use_cases.create_buy(client_id, food_name)
            return HttpResponse.success('Successfully registered buy!', response.__dict__)
        except RabbitMQError as error:
            return HttpResponse.internal_error(message=str(error))
