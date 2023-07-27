from src.domain.interfaces.user_interface import UserStorage
from src.domain.models.user_model import UserModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.config.config_storage import ConfigStorage
from src.infrastructure.service.mysql import MySQL


class UserStorageMySQL(MySQL, UserStorage):
    def __init__(self):
        super(UserStorageMySQL, self).__init__(ConfigStorage)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS clients ("
            "client_id VARCHAR(36) PRIMARY KEY,"
            "name VARCHAR(255) NOT NULL,"
            "email VARCHAR(255) NOT NULL,"
            "address VARCHAR(255) NOT NULL"
            ")"
        )

        self.execute_query_one(create_table_query)
        self.commit()

    def get_all(self):
        get_all_query = "SELECT * FROM clients"

        if clients := self.execute_query_many(get_all_query):
            return [UserModel(*user) for user in clients]
        else:
            raise NotFoundFail('Client not found')

    def get_by_id(self, client_id, return_fields="*"):
        get_by_id_query = f"SELECT {return_fields} FROM clients WHERE client_id = %s"
        get_by_id_params = (client_id,)
        data_client = self.execute_query_one(get_by_id_query, get_by_id_params)

        if data_client and return_fields == "*":
            return UserModel(*data_client)
        elif data_client and return_fields != "*":
            return data_client
        else:
            raise NotFoundFail('Client not found')

    def save(self, user: UserModel):
        save_query = "INSERT INTO clients (client_id, name, email, address) VALUES (%s, %s, %s, %s)"
        save_params = (user.client_id, user.name, user.email, user.address)

        self.execute_query_one(save_query, save_params)
        self.commit()
        self.connection_close()
