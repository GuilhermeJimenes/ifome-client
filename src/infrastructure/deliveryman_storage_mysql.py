from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.config.config_storage import ConfigStorage
from src.infrastructure.service.mysql import MySQL


class DeliverymanStorageMySQL(MySQL, DeliverymanStorage):
    def __init__(self):
        super(DeliverymanStorageMySQL, self).__init__(ConfigStorage)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliverymans ("
            "deliveryman_id VARCHAR(36) PRIMARY KEY,"
            "name VARCHAR(255) NOT NULL,"
            "email VARCHAR(255) NOT NULL,"
            "available BOOLEAN NOT NULL DEFAULT TRUE"
            ")"
        )

        self.execute_query_one(create_table_query)
        self.commit()

    def get_available(self):
        get_available_query = "SELECT deliveryman_id FROM deliverymans WHERE available = true ORDER BY RAND() LIMIT 1"

        if deliverymans := self.execute_query_one(get_available_query):
            return deliverymans
        else:
            raise NotFoundFail('Deliveryman not found')

    def update(self, deliveryman_id):
        update_query = "UPDATE deliverymans SET available = false WHERE deliveryman_id = %s"
        update_params = (deliveryman_id, )

        self.execute_query_one(update_query, update_params)
        self.commit()
        self.connection_close()
