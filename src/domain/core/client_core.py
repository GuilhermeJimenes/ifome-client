from src.domain.interfaces.client_interface import ClientStorage
from src.domain.models.client_model import ClientModel
from src.exceptions.custom_exceptions import InvalidInputFail
from src.utils.email import is_valid_email
from src.utils.parser import create_hash


class GetAllClientsCore:
    def __init__(self, client_storage: ClientStorage):
        self.client_storage = client_storage

    def get_all_clients(self):
        return self.client_storage.get_all()


class GetClientByIdCore:
    def __init__(self, client_storage: ClientStorage):
        self.client_storage = client_storage

    def get_client_by_id(self, client_id):
        return self.client_storage.get_by_id(client_id)


class CreateClientCore:
    def __init__(self, client_storage: ClientStorage):
        self.client_storage = client_storage

    def validate_client_credential(self, email):
        if not is_valid_email(email):
            raise InvalidInputFail("Invalid email.")

    def new_client(self, name, email, address):
        client_id = create_hash(email)
        return ClientModel(client_id, name, email, address)

    def create_client(self, name, email, address):
        self.validate_client_credential(email)
        client = self.new_client(name, email, address)
        self.client_storage.save(client)
        return client
