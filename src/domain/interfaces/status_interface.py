class StatusMessageBroker:

    def consume_status(self):
        raise NotImplementedError()

    def consume_success(self):
        raise NotImplementedError()

    def close_connection(self):
        raise NotImplementedError()
