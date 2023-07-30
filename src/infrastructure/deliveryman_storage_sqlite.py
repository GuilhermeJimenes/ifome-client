from src.domain.constants import STORAGE_SQLITE_PATH
from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class DeliverymanStorageSQLite(SQLite, DeliverymanStorage):
    def __init__(self):
        super(DeliverymanStorageSQLite, self).__init__(STORAGE_SQLITE_PATH)

    def get_available(self):
        get_available_query = "SELECT deliveryman_id FROM deliverymans WHERE available = true ORDER BY RAND() LIMIT 1"

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
