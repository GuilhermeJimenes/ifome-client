from src.infrastructure.status_message_broker_rabbitmq import StatusMessageBrokerRabbitMQ

from src.domain.constants import MESSAGE_BROKER_TYPE
from src.domain.core.status_core import StatusCore
from src.domain.interfaces.status_interface import StatusMessageBroker
from src.exceptions.custom_exceptions import RabbitMQError, NotFoundFail


class StatusApp:
    def __init__(self):
        if MESSAGE_BROKER_TYPE == "rabbitmq":
            self.status_message_broker: StatusMessageBroker = StatusMessageBrokerRabbitMQ()
        else:
            raise ValueError("Invalid message broker, valid types: rabbitmq")

    def status(self):
        try:
            status_core = StatusCore(self.status_message_broker)
            response = status_core.status()
            self.status_message_broker.consume_success()
            return response
        except NotFoundFail as error:
            print(error)
            self.status_message_broker.close_connection()
            return 'error'
        except KeyboardInterrupt as error:
            print(error)
            self.status_message_broker.close_connection()
            return 'error'
        except RabbitMQError as error:
            print(error)
            self.status_message_broker.close_connection()
            return 'error'
