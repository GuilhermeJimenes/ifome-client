from src.domain.constants import STORAGE_SQLITE_PATH
from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class DeliverymanStorageSQLite(SQLite, DeliverymanStorage):
    def __init__(self):
        super(DeliverymanStorageSQLite, self).__init__(STORAGE_SQLITE_PATH)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliverymans ("
            "deliveryman_id TEXT PRIMARY KEY,"
            "name TEXT NOT NULL,"
            "email TEXT NOT NULL,"
            "available INTEGER NOT NULL DEFAULT 1"
            ")"
        )

        self.execute_query_one(create_table_query)

    def get_available(self):
        get_available_query = "SELECT deliveryman_id FROM deliverymans WHERE available = true ORDER BY RANDOM() LIMIT 1"

        if deliverymans := self.execute_query_one(get_available_query):
            return deliverymans
        else:
            raise NotFoundFail('Deliveryman not found')

    def update(self, deliveryman_id):
        update_query = "UPDATE deliverymans SET available = 0 WHERE deliveryman_id = %s"
        update_params = (deliveryman_id, )

        self.execute_query_one(update_query, update_params)
        self.commit()
        self.connection_close()
