class ClientStorage:
    def create_table(self):
        raise NotImplementedError()

    def get_all(self):
        raise NotImplementedError()

    def get_by_id(self, client_id, return_fields="*"):
        raise NotImplementedError()

    def save(self, user):
        raise NotImplementedError()
