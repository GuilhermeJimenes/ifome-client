from src.api.http.http_response import HttpResponse
from src.domain.constants import STORAGE_TYPE
from src.domain.core.user_core import GetAllUsersCore, GetUserByIdCore, CreateUserCore
from src.domain.interfaces.user_interface import UserStorage
from src.exceptions.custom_exceptions import NotFoundFail, InvalidInputFail, RabbitMQError
from src.infrastructure.user_storage_mysql import UserStorageMySQL
from src.infrastructure.user_storage_sqlite import UserStorageSQLite


class UserApp:
    def __init__(self):
        if STORAGE_TYPE == "mysql":
            self.user_storage: UserStorage = UserStorageMySQL()
        elif STORAGE_TYPE == "sqlite":
            self.user_storage: UserStorage = UserStorageSQLite()
        else:
            raise ValueError("Invalid storage, valid types: sqlite, mysql")

    def get_all_users(self):
        try:
            user_use_cases = GetAllUsersCore(self.user_storage)
            response = [user.__dict__ for user in user_use_cases.get_all_users()]
            return HttpResponse.success('Clients found successfully!', response)
        except NotFoundFail as error:
            return HttpResponse.failed(message=str(error))

    def get_user_by_id(self, client_id):
        try:
            user_use_cases = GetUserByIdCore(self.user_storage)
            response = user_use_cases.get_user_by_id(client_id)
            return HttpResponse.success('Client found successfully!', response.__dict__)
        except NotFoundFail as error:
            return HttpResponse.failed(message=str(error))

    def create_user(self, name, email, address):
        try:
            user_use_cases = CreateUserCore(self.user_storage)
            response = user_use_cases.create_user(name, email, address)
            return HttpResponse.success('Successfully registered client!', response.__dict__)
        except InvalidInputFail as error:
            return HttpResponse.failed(message=str(error))
        except RabbitMQError as error:
            return HttpResponse.internal_error(message=str(error))
