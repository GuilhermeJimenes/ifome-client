from src.domain.constants import STORAGE_SQLITE_PATH, TABLE_SQLITE_DELIVERY
from src.domain.interfaces.buy_interface import BuyStorage
from src.domain.models.delivery_model import DeliveryModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class BuyStorageSQLite(SQLite, BuyStorage):
    def __init__(self):
        table_path = f"{STORAGE_SQLITE_PATH}{TABLE_SQLITE_DELIVERY}"
        super(BuyStorageSQLite, self).__init__(table_path)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliverys ("
            "delivery_id TEXT PRIMARY KEY,"
            "client_id TEXT PRIMARY KEY,"
            "food_name TEXT NOT NULL,"
            "address TEXT NOT NULL"
            ")"
        )

        self.execute_query_one(create_table_query)

    def get_by_id(self, delivery_id, return_fields="*"):
        get_by_id_query = f"SELECT {return_fields} FROM clients WHERE delivery_id = ?"
        get_by_id_params = (delivery_id,)

        data_client = self.execute_query_one(get_by_id_query, get_by_id_params)

        if data_client and return_fields == "*":
            return DeliveryModel(*data_client)
        elif data_client and return_fields != "*":
            return data_client
        else:
            raise NotFoundFail('Client not found')

    def save(self, delivery: DeliveryModel):
        save_query = "INSERT INTO deliverys (delivery_id, client_id, name, address) VALUES (?, ?, ?, ?)"
        save_params = (delivery.delivery_id, delivery.client_id, delivery.food_name, delivery.address)

        self.execute_query_one(save_query, save_params)
        self.commit()
