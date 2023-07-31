from src.domain.constants import STORAGE_SQLITE_PATH
from src.domain.interfaces.client_interface import ClientStorage
from src.domain.models.client_model import ClientModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class ClientsStorageSQLite(SQLite, ClientStorage):
    def __init__(self):
        super(ClientsStorageSQLite, self).__init__(STORAGE_SQLITE_PATH)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS clients ("
            "client_id TEXT PRIMARY KEY,"
            "name TEXT NOT NULL,"
            "email TEXT NOT NULL,"
            "address TEXT NOT NULL"
            ")"
        )

        self.execute_query_one(create_table_query)

    def get_all(self):
        get_all_query = "SELECT * FROM clients"

        if clients := self.execute_query_many(get_all_query):
            return [ClientModel(*user) for user in clients]
        else:
            raise NotFoundFail('Client not found')

    def get_by_id(self, client_id, return_fields="*"):
        get_by_id_query = f"SELECT {return_fields} FROM clients WHERE client_id = ?"
        get_by_id_params = (client_id,)
        data_client = self.execute_query_one(get_by_id_query, get_by_id_params)

        if data_client and return_fields == "*":
            return ClientModel(*data_client)
        elif data_client and return_fields != "*":
            return data_client
        else:
            raise NotFoundFail('Client not found')

    def save(self, user: ClientModel):
        save_query = "INSERT INTO clients (client_id, name, email, address) VALUES (?, ?, ?, ?)"
        save_params = (user.client_id, user.name, user.email, user.address)

        self.execute_query_one(save_query, save_params)
        self.commit()
