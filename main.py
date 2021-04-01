import atexit
from getpass import getpass
from datetime import date

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

    def insert_data(self, query, data):
        self.cursor.execute(query, data)
        self.connection.commit()


class SalaryInterface(MyConnector):
    """ Interface for simple access sql functionality """
    def __init__(self, param):
        super().__init__(param)

    def show_table(self, table):
        query = f"SELECT * FROM {table}"
        self.query_exe(query)
        for row in self.cursor:
            print(row)

    def add_employee(self, data):
        query = "INSERT INTO employee (name, positionId) VALUES (%(name)s, %(positionId)s)"
        self.insert_data(query, data)

    def add_employee_schedule(self, data):
        query = "INSERT INTO schedule (employeeId, date, hours) VALUES (%(employeeId)s, %(date)s, %(hours)s)"
        self.insert_data(query, data)


def main():

    try:
        salary = SalaryInterface({
                'host': 'localhost',
                'user': 'root',
                'password': getpass(),
                'database': 'salary_calc'}
        )

        # salary.add_employee({'name': 'Stanislav G', 'positionId': 2})
        today = date(2020, 3, 27)
        salary.add_employee_schedule({'employeeId': '1', 'date': today, 'hours': 8})
        salary.show_table('employee')
        salary.show_table('schedule')

    except Error as e:
        print(e)


if __name__ == '__main__':
    main()
