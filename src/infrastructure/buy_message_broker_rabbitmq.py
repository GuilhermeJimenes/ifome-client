from src.domain.constants import BUY_QUEUE
from src.domain.interfaces.deliveries_interface import BuyMessageBroker
from src.infrastructure.service.rabbitmq import RabbitMQ


class BuyMessageBrokerRabbitMQ(RabbitMQ, BuyMessageBroker):
    queue_name = BUY_QUEUE

    def send_buy(self, message):
        self.new_queue(self.queue_name)
        self.publish(self.queue_name, message)

    def view_status(self):
        self.new_queue(self.queue_name)
        self.consume(self.queue_name)

