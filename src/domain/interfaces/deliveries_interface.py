class DeliveriesStorage:
    def create_table(self):
        raise NotImplementedError()

    def get_by_id(self, client_id, return_fields="*"):
        raise NotImplementedError()

    def save(self, delivery):
        raise NotImplementedError()


class BuyMessageBroker:
    def send_buy(self, message):
        raise NotImplementedError()

    def view_status(self):
        raise NotImplementedError()

    def connection_close(self):
        raise NotImplementedError()
