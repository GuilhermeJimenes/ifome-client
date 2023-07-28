from sqlite3 import connect


class SQLite:
    def __init__(self, storege_path):
        self.connection = connect(storege_path)

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
