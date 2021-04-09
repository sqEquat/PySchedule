import sys
import os

from PyQt5 import QtWidgets, QtGui, QtCore
from design import Ui_MainWindow

from main import SalaryInterface


class SalaryGui(SalaryInterface):
    def __init__(self, param, ui):
        super().__init__(param)

        self.ui = ui
        self.table_by_index = [
            ('employee', ui.employeesTable),
            ('schedule', ui.scheduleTable),
            ('payment', ui.paymentsTable),
            ('position', ui.positionsTable)
        ]

    def show_table(self, table_index):
        table_name = self.table_by_index[table_index][0]
        table_data = self.get_table(table_name)
        table_shape = table_data[0]
        table_rows = table_data[1]

        table_gui = self.table_by_index[table_index][1]
        table_gui.setColumnCount(table_shape[1])
        table_gui.setRowCount(table_shape[0])
        for row, tup in enumerate(table_rows):
            for col, item in enumerate(tup):
                cell_value = QtWidgets.QTableWidgetItem(str(item))
                cell_value.setTextAlignment(QtCore.Qt.AlignCenter)
                table_gui.setItem(row, col, cell_value)

    def tab_changed(self):
        self.show_table(self.ui.tabBar.currentIndex())


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

        self.ui.tabBar.currentChanged.connect(self.salary.tab_changed)


def main():
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
