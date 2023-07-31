from src.domain.constants import BUY_QUEUE
from src.domain.interfaces.deliveries_interface import BuyMessageBroker
from src.infrastructure.service.rabbitmq import RabbitMQ


class BuyMessageBrokerRabbitMQ(RabbitMQ, BuyMessageBroker):
    def publish_buy(self, message):
        self.new_queue(BUY_QUEUE)
        self.publish(BUY_QUEUE, message)

