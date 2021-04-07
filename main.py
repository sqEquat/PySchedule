import calendar
import os
import datetime as dt
import calendar as cld

from getpass import getpass
from mysql.connector import Error

from myconnector import MyConnector


class SalaryInterface(MyConnector):
    """ Interface for simple access sql functionality """
    def __init__(self, param):
        super().__init__(param)

    def show_table(self, table):
        query = f"SELECT * FROM {table}"
        self.select_query(query)
        for row in self.cursor:
            print(row)

    def add_employee(self, data):
        query = "INSERT INTO employee (name, positionId) VALUES (%(name)s, %(positionId)s)"
        self.insert_query(query, data)

    def add_employee_schedule(self, data):
        query = "INSERT INTO schedule (employeeId, date, hours) VALUES (%(employeeId)s, %(date)s, %(hours)s)"
        self.insert_query(query, data)

    def get_position_rate(self, employee_id):
        query = f"""SELECT rate FROM salary_calc.position 
                    WHERE id = (SELECT positionId FROM employee WHERE id = {employee_id})"""
        self.select_query(query)

        # fetchone return a tuple with one value, so [0] gets the value
        return self.cursor.fetchone()[0]

    def fill_schedule(self, employee_id, year, month, hours):
        cal = calendar.Calendar()
        for day in cal.itermonthdates(year, month):
            data = {'employeeId': employee_id, 'date': day, 'hours': hours}
            self.add_employee_schedule(data)

    def calc_salary(self, employee_id, month, nominal_hours):
        pass


def main():

    try:
        salary = SalaryInterface({
                'host': 'localhost',
                'user': 'root',
                'password': os.environ.get('SQL_CONNECTOR_PASS'),
                'database': 'salary_calc'}
        )

        # salary.fill_schedule(1, 2021, 4, 8)
        # salary.show_table('schedule')

    except Error as e:
        print(e)


if __name__ == '__main__':
    main()
