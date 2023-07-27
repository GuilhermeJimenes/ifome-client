from src.domain.constants import STORAGE_SQLITE_PATH, TABLE_SQLITE_CLIENTS
from src.domain.interfaces.user_interface import UserStorage
from src.domain.models.user_model import UserModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class UserStorageSQLite(SQLite, UserStorage):
    def __init__(self):
        table_path = f"{STORAGE_SQLITE_PATH}{TABLE_SQLITE_CLIENTS}"
        super(UserStorageSQLite, self).__init__(table_path)
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
            return [UserModel(*user) for user in clients]
        else:
            raise NotFoundFail('Client not found')

    def get_by_id(self, client_id, return_fields="*"):
        get_by_id_query = f"SELECT {return_fields} FROM clients WHERE client_id = ?"
        get_by_id_params = (client_id,)
        data_client = self.execute_query_one(get_by_id_query, get_by_id_params)

        if data_client and return_fields == "*":
            return UserModel(*data_client)
        elif data_client and return_fields != "*":
            return data_client
        else:
            raise NotFoundFail('Client not found')

    def save(self, user: UserModel):
        save_query = "INSERT INTO clients (client_id, name, email, address) VALUES (?, ?, ?, ?)"
        save_params = (user.client_id, user.name, user.email, user.address)

        self.execute_query_one(save_query, save_params)
        self.commit()
