from getpass import getpass
from datetime import date
from mysql.connector import Error

from myconnector import MyConnector


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

    def get_position_rate(self, employee_id):
        query = f"""SELECT rate FROM salary_calc.position 
                    WHERE id = (SELECT positionId FROM employee WHERE id = {employee_id})"""
        self.query_exe(query)

        return [x for x in self.cursor][0][0]

    def calc_salary(self, employee_id, month, nominal_hours):
        pass


def main():

    try:
        salary = SalaryInterface({
                'host': 'localhost',
                'user': 'root',
                'password': getpass(),
                'database': 'salary_calc'}
        )

        # salary.add_employee({'name': 'Stanislav G', 'positionId': 2})
        # today = date(2020, 3, 27)
        # salary.add_employee_schedule({'employeeId': '1', 'date': today, 'hours': 8})
        # salary.show_table('employee')
        # salary.show_table('schedule')
        rate = salary.get_position_rate(1)
        print(rate)

    except Error as e:
        print(e)


if __name__ == '__main__':
    main()
