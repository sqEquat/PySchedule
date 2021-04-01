# This is a sample Python script.
from getpass import getpass
from mysql.connector import connect, Error

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    try:
        with connect(
            host='localhost',
            user='root',
            password=getpass(),
            database='salary_calc'
        ) as connection:
            print(connection)
            query = "SELECT * FROM salary_calc.employee"
            with connection.cursor() as cursor:
                cursor.execute(query)
                for row in cursor:
                    print(row)

    except Error as e:
        print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
