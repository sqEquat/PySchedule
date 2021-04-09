import sys
import os

from PyQt5 import QtWidgets, QtGui, QtCore
from design import Ui_MainWindow

from main import SalaryInterface


class SalaryGui(SalaryInterface):
    def __init__(self, param, ui):
        super().__init__(param)

        self.ui = ui
        self.tab_tables_dict = {
            'employee': ui.employeesTable,
            'schedule': ui.scheduleTable,
            'payments': ui.positionsTable
        }

    def show_table(self, table_name):
        table_data = self.get_table(table_name)
        table_shape = table_data[0]
        table = table_data[1]

        table_gui = self.tab_tables_dict[table_name]
        table_gui.setColumnCount(table_shape[1])
        table_gui.setRowCount(table_shape[0])
        for row, tup in enumerate(table):
            for col, item in enumerate(tup):
                cell_value = QtWidgets.QTableWidgetItem(str(item))
                cell_value.setTextAlignment(QtCore.Qt.AlignCenter)
                table_gui.setItem(row, col, cell_value)
                table_gui.res


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.salary = SalaryGui({
                'host': 'localhost',
                'user': 'root',
                'password': os.environ.get('SQL_CONNECTOR_PASS'),
                'database': 'salary_calc'
        }, self.ui)

        self.salary.show_table('employee')


def main():
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
