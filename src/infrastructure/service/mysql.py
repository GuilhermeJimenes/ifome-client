from mysql.connector import connect


class MySQL:
    def __init__(self, config_storage):
        self.connection = connect(
            host=config_storage.HOST,
            user=config_storage.USER,
            password=config_storage.PASSWORD,
            database=config_storage.DATABASE
        )

    def execute_query_one(self, query: str, params: tuple = ()):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result

    def execute_query_many(self, query: str, params: tuple = ()):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result

    def commit(self):
        self.connection.commit()

    def connection_close(self):
        self.connection.close()
