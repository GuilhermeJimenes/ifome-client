from src.domain.constants import DELIVERY_QUEUE_NAME
from src.domain.interfaces.buy_interface import BuyMessageBroker
from src.infrastructure.service.rabbitmq import RabbitMQ


class BuyMessageBrokerRabbitMQ(RabbitMQ, BuyMessageBroker):
    queue_name = DELIVERY_QUEUE_NAME

    def send_buy(self, message):
        self.new_queue(self.queue_name)
        self.publish(self.queue_name, message)

    def view_status(self):
        self.new_queue(self.queue_name)
        self.consume(self.queue_name)

