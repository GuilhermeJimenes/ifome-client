from src.domain.constants import STATUS_QUEUE
from src.domain.interfaces.status_interface import StatusMessageBroker
from src.infrastructure.service.rabbitmq import RabbitMQ


class StatusMessageBrokerRabbitMQ(RabbitMQ, StatusMessageBroker):
    def consume_status(self):
        return self.start_consuming(STATUS_QUEUE)
