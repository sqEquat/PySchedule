import atexit
from getpass import getpass
from mysql.connector import connect, Error


class MyConnector:
    """ Wrapper for connector from mysql.connector """
    def __init__(self, param):
        self.connection = connect(**param)
        self.cursor = self.connection.cursor(buffered=True)

        atexit.register(self.cursor.close)
        atexit.register(self.connection.close)

    def query_exe(self, query):
        self.cursor.execute(query)
        self.connection.commit()


def main():

    try:
        connection = MyConnector({
                'host': 'localhost',
                'user': 'root',
                'password': getpass(),
                'database': 'salary_calc'}
        )

        query = "SELECT * FROM salary_calc.employee"
        connection.query_exe(query)
        for row in connection.cursor:
            print(row)

    except Error as e:
        print(e)


if __name__ == '__main__':
    main()
