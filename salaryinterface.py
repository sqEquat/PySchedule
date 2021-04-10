import os

from datetime import date
from calendar import Calendar
from mysql.connector import Error

from myconnector import MyConnector


class SalaryInterface(MyConnector):
    """ Interface for simple access sql functionality """

    def __init__(self, param):
        super().__init__(param)

    def get_table(self, table):
        """ Return table shape and table data """

        query = f"SELECT * FROM {table}"
        self.select_query(query)
        table = self.cursor.fetchall()

        result = [(len(table), len(table[0])), table]
        return result

    def get_table_header(self, table):
        """ Return titles of columns """

        query = f"SHOW columns FROM {table}"

        self.select_query(query)
        header = self.cursor.fetchall()
        return [row[0] for row in header]

    def add_employee(self, name, position_id):
        """ Add new employee """

        query = f"INSERT INTO employee (name, positionId) VALUES ('{name}', {position_id})"
        self.insert_query(query)

    def del_employee(self, employee_id):
        query = f"DELETE FROM employee WHERE id = {employee_id}"
        self.delete_query(query)

    def add_employee_schedule(self, employee_id, sch_date, hours):
        """ Insert row with worked out hours of employee at the date """

        query = f"""INSERT INTO schedule (employeeId, date, hours)
                    VALUES ({employee_id}, '{sch_date}', {hours})"""
        self.insert_query(query)

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
                data = {'employee_id': employee_id, 'date': day, 'hours': hours}
                self.add_employee_schedule(data)

    def get_total_month_worked_out_hours(self, employee_id, year, month):
        """ Return sum of hours from schedule table  of employee in the month of the year """

        query = f"""SELECT SUM(sch.hours) FROM schedule sch
                    WHERE MONTH(sch.date) = {month} AND YEAR(sch.date) = {year} AND sch.employeeId = {employee_id}"""
        self.select_query(query)

        # fetchone() return a tuple with one value, so [0] gets the value
        return self.cursor.fetchone()[0]

    def calc_salary(self, data):
        """ Insert row with information of employee payment in tne month of the year  """

        employee_id = data['employee_id']
        payment_date = date.today()
        total_hours = self.get_total_month_worked_out_hours(employee_id, data['year'], data['month'])
        nominal_hours = data['nominal_hours']
        rate = self.get_position_rate(employee_id)
        payment_sum = (total_hours / nominal_hours) * rate
        status_id = 2

        query = f"""INSERT INTO payment (employeeId, date, totalHours, nominalHours, positionRate, sum, statusId)
                    VALUES ({employee_id}, '{payment_date}', {total_hours}, {nominal_hours}, {rate}, {payment_sum:.2f}, {status_id})"""
        self.insert_query(query)

    def get_position_list(self):
        query = "SELECT title FROM position"
        self.select_query(query)

        return [pos[0] for pos in self.cursor.fetchall()]


def main():

    try:
        salary = SalaryInterface({
                'host': 'localhost',
                'user': 'root',
                'password': os.environ.get('SQL_CONNECTOR_PASS'),
                'database': 'salary_calc'}
        )

        # salary.add_employee({'name': 'Anton C', 'position_id': 1})
        # salary.fill_schedule(12, 2021, 4, 5)
        # salary.show_table('schedule')

        # salary.calc_salary({'employee_id': 1, 'month': 4, 'year': 2021, 'nominal_hours': 160})

        salary.del_employee(17)

    except Error as e:
        print(e)


if __name__ == '__main__':
    main()
