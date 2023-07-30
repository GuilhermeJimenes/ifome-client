class DeliveriesStorage:
    def create_table(self):
        raise NotImplementedError()

    def get_by_id(self, client_id, return_fields="*"):
        raise NotImplementedError()

    def save(self, delivery):
        raise NotImplementedError()


class BuyMessageBroker:
    def publish_buy(self, message):
        raise NotImplementedError()

    def consume_success(self):
        raise NotImplementedError()

    def close_connection(self):
        raise NotImplementedError()

