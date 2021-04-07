from calendar import Calendar
import os

from getpass import getpass
from mysql.connector import Error

from myconnector import MyConnector


class SalaryInterface(MyConnector):
    """ Interface for simple access sql functionality """
    def __init__(self, param):
        super().__init__(param)

    def show_table(self, table):
        """ Display all rows of the table """
        query = f"SELECT * FROM {table}"
        self.select_query(query)
        for row in self.cursor:
            print(row)

    def add_employee(self, data):
        """ Add new employee """

        query = "INSERT INTO employee (name, positionId) VALUES (%(name)s, %(positionId)s)"
        self.insert_query(query, data)

    def add_employee_schedule(self, data):
        """ Insert row with worked out hours of employee at the date """

        query = "INSERT INTO schedule (employeeId, date, hours) VALUES (%(employeeId)s, %(date)s, %(hours)s)"
        self.insert_query(query, data)

    def get_position_rate(self, employee_id):
        """ Return position rate of the employee """

        query = f"""SELECT rate FROM salary_calc.position 
                    WHERE id = (SELECT positionId FROM employee WHERE id = {employee_id})"""
        self.select_query(query)

        # fetchone() return a tuple with one value, so [0] gets the value
        return self.cursor.fetchone()[0]

    def fill_schedule(self, employee_id, year, month, hours):
        """ Fill every work day of the month worked out hours of employee """

        cal = Calendar()
        for day in cal.itermonthdates(year, month):
            if day.weekday() < 5:   # 5 is a Saturday
                data = {'employeeId': employee_id, 'date': day, 'hours': hours}
                self.add_employee_schedule(data)

    def get_total_month_worked_out_hours(self, employee_id, year, month):
        """ Return sum of hours from schedule table  of employee in the month of the year """

        query = f"""select sum(sch.hours) from schedule sch
                    where month(sch.date) = {month} and year(sch.date) = {year} and sch.employeeId = {employee_id}"""
        self.select_query(query)

        # fetchone() return a tuple with one value, so [0] gets the value
        return self.cursor.fetchone()[0]

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

        # salary.fill_schedule(2, 2021, 4, 8)
        # salary.show_table('schedule')

        print(salary.get_total_month_worked_out_hours(1, 2021, 4))

    except Error as e:
        print(e)


if __name__ == '__main__':
    main()
