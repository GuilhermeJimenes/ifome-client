from src.api.http.http_response import HttpResponse
from src.domain.constants import STORAGE_TYPE
from src.domain.core.client_core import GetAllClientsCore, GetClientByIdCore, CreateClientCore
from src.domain.interfaces.client_interface import ClientStorage
from src.exceptions.custom_exceptions import NotFoundFail, InvalidInputFail, RabbitMQError
from src.infrastructure.clients_storage_mysql import ClientsStorageMySQL
from src.infrastructure.clients_storage_sqlite import ClientsStorageSQLite


class ClientApp:
    def __init__(self):
        if STORAGE_TYPE == "mysql":
            self.client_storage: ClientStorage = ClientsStorageMySQL()
        elif STORAGE_TYPE == "sqlite":
            self.client_storage: ClientStorage = ClientsStorageSQLite()
        else:
            raise ValueError("Invalid storage, valid types: sqlite, mysql")

    def get_all_clients(self):
        try:
            client_core = GetAllClientsCore(self.client_storage)
            response = [client.__dict__ for client in client_core.get_all_clients()]
            return HttpResponse.success('Clients found successfully!', response)
        except NotFoundFail as error:
            return HttpResponse.failed(message=str(error))

    def get_client_by_id(self, client_id):
        try:
            client_core = GetClientByIdCore(self.client_storage)
            response = client_core.get_client_by_id(client_id)
            return HttpResponse.success('Client found successfully!', response.__dict__)
        except NotFoundFail as error:
            return HttpResponse.failed(message=str(error))

    def create_client(self, name, email, address):
        try:
            client_core = CreateClientCore(self.client_storage)
            response = client_core.create_client(name, email, address)
            return HttpResponse.success('Successfully registered client!', response.__dict__)
        except InvalidInputFail as error:
            return HttpResponse.failed(message=str(error))
        except RabbitMQError as error:
            return HttpResponse.internal_error(message=str(error))
