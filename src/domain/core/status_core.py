from src.domain.interfaces.status_interface import StatusMessageBroker


class StatusCore:
    def __init__(self, status_message_broker: StatusMessageBroker):
        self.status_message_broker = status_message_broker

    def get_status(self):
        return self.status_message_broker.consume_status()

    def status(self):
        delivery_status = self.get_status()
        return delivery_status
