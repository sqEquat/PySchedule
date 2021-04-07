import atexit
from mysql.connector import connect


class MyConnector:
    """ Wrapper for connector from mysql.connector """
    def __init__(self, param):
        self.connection = connect(**param)
        self.cursor = self.connection.cursor(buffered=True)

        atexit.register(self.cursor.close)
        atexit.register(self.connection.close)

    def insert_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def select_query(self, query):
        self.cursor.execute(query)
