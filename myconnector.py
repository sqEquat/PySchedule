import atexit
from mysql.connector import connect


class MyConnector:
    """ Wrapper for connector from mysql.connector """
    def __init__(self, param):
        self.connection = connect(**param)
        self.cursor = self.connection.cursor(buffered=True)

        atexit.register(self.cursor.close)
        atexit.register(self.connection.close)

    def query_exe(self, query, data=None):
        self.cursor.execute(query, data)
        self.connection.commit()
