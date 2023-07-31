from src.domain.interfaces.deliveries_interface import DeliveriesStorage
from src.domain.models.delivery_model import DeliveryModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.config.config_storage import ConfigStorage
from src.infrastructure.service.mysql import MySQL


class DeliveriesStorageMySQL(MySQL, DeliveriesStorage):
    def __init__(self):
        super(DeliveriesStorageMySQL, self).__init__(ConfigStorage)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliveries ("
            "delivery_id VARCHAR(255) PRIMARY KEY,"
            "client_id VARCHAR(255) NOT NULL,"
            "food_name VARCHAR(255) NOT NULL,"
            "address VARCHAR(255) NOT NULL,"
            "deliveryman_id VARCHAR(255) DEFAULT '',"
            "status VARCHAR(255) DEFAULT ''"
            ")"
        )

        self.execute_query_one(create_table_query)
        self.commit()

    def get_by_id(self, delivery_id, return_fields="*"):
        get_by_id_query = f"SELECT {return_fields} FROM deliveries WHERE delivery_id = %s"
        get_by_id_params = (delivery_id,)

        data_client = self.execute_query_one(get_by_id_query, get_by_id_params)

        if data_client and return_fields == "*":
            return DeliveryModel(*data_client)
        elif data_client and return_fields != "*":
            return data_client
        else:
            raise NotFoundFail('Delivery not found')

    def save(self, delivery: DeliveryModel):
        save_query = "INSERT INTO deliveries (delivery_id, client_id, food_name, address, deliveryman_id, " \
                     "status) VALUES (%s, %s, %s, %s, %s, %s)"
        save_params = (delivery.delivery_id, delivery.client_id, delivery.food_name,
                       delivery.address, delivery.deliveryman_id, delivery.status)

        self.execute_query_one(save_query, save_params)
        self.commit()
        self.connection_close()
