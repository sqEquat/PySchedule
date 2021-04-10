import sys
import os

from PyQt5 import QtWidgets, QtGui, QtCore
from design.mainwindow import Ui_MainWindow
from design.addemployee import Ui_AddEmployee
from design.addschedule import Ui_AddSchedule

from salaryinterface import SalaryInterface


class SalaryGui(SalaryInterface):
    def __init__(self, param, ui):
        super().__init__(param)

        self.ui = ui
        self.table_by_index = [
            ('employee', ui.employeesTable),
            ('schedule', ui.schedulesTable),
            ('payment', ui.paymentsTable),
            ('position', ui.positionsTable),
            ('paymentstatus', ui.payStatusTable)
        ]

    def show_table(self, table_index):
        table_name = self.table_by_index[table_index][0]
        table_data = self.get_table(table_name)
        table_header = self.get_table_header(table_name)
        table_shape = table_data[0]
        table_rows = table_data[1]

        table_gui = self.table_by_index[table_index][1]
        table_gui.setColumnCount(table_shape[1])
        table_gui.setRowCount(table_shape[0])
        table_gui.setHorizontalHeaderLabels(table_header)
        for row, tup in enumerate(table_rows):
            for col, item in enumerate(tup):
                cell_value = QtWidgets.QTableWidgetItem(str(item))
                cell_value.setTextAlignment(QtCore.Qt.AlignCenter)
                table_gui.setItem(row, col, cell_value)

        table_gui.resizeColumnsToContents()


class AddEmployeeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddEmployee()
        self.ui.setupUi(self)


class AddSchedule(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddSchedule()
        self.ui.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.window = None

        self.salary = SalaryGui({
                'host': 'localhost',
                'user': 'root',
                'password': os.environ.get('SQL_CONNECTOR_PASS'),
                'database': 'salary_calc'
        }, self.ui)

        self.tab_to_window = [AddEmployeeWindow, AddSchedule]

        self.ui.tabBar.setCurrentIndex(0)
        self.salary.show_table(0)

        self.ui.tabBar.currentChanged.connect(self.tab_changed)
        self.ui.addButton.clicked.connect(self.open_window)

    def tab_changed(self):
        tab_index = self.ui.tabBar.currentIndex()
        self.salary.show_table(tab_index)

    def open_window(self):
        tab_index = self.ui.tabBar.currentIndex()
        self.window = self.tab_to_window[tab_index]()
        self.window.show()


def main():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
