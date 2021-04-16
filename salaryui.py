import sys
import os

from PyQt5 import QtWidgets, QtCore
from design.mainwindow import Ui_MainWindow
from design.addemployee import Ui_AddEmployee
from design.addschedule import Ui_AddSchedule

from mysql.connector import Error

from salaryinterface import SalaryInterface


class SalaryGui(SalaryInterface):
    """ Connector between main window gui and salary connector """
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
        table_shape = (self.get_table_shape(table_name))
        table_header = self.get_table_header(table_name)
        table_data = self.get_table(table_name)

        table_gui = self.table_by_index[table_index][1]

        table_gui.setColumnCount(table_shape[0])
        table_gui.setRowCount(table_shape[1])

        table_gui.setHorizontalHeaderLabels(table_header)
        for row, tup in enumerate(table_data):
            for col, item in enumerate(tup):
                cell_value = QtWidgets.QTableWidgetItem(str(item))
                cell_value.setTextAlignment(QtCore.Qt.AlignCenter)
                table_gui.setItem(row, col, cell_value)

        table_gui.resizeColumnsToContents()

    def delete_row(self, table_index):
        table_name = self.table_by_index[table_index][0]
        table_gui = self.table_by_index[table_index][1]
        try:
            for index in table_gui.selectedIndexes():
                row = index.row()
                item_id = table_gui.item(row, 0).text()
                self.del_by_id(table_name, item_id)
        except Error as e:
            self.ui.statusBar.showMessage(str(e))

        self.show_table(table_index)


class AddEmployeeWindow(QtWidgets.QMainWindow):
    """ Add new row into employee window """
    def __init__(self, salary):
        super().__init__()
        self.ui = Ui_AddEmployee()
        self.ui.setupUi(self)

        self.salary = salary
        self.position = self.salary.get_table('position')[1]
        self.set_position_combobox()

        self.ui.add_button.clicked.connect(self.add_employee)
        self.ui.cancel_button.clicked.connect(self.cancel)

    def add_employee(self):
        name = self.ui.employee_name_line.text()
        # Position list contains tuple (position_id, title, rate),
        # combobox index is equal list index and [0] return position_id
        position_id = self.position[self.ui.position_combobox.currentIndex()][0]
        self.salary.add_employee(name, position_id)
        self.salary.show_table(self.salary.ui.tabBar.currentIndex())
        self.close()

    def cancel(self):
        self.close()

    def set_position_combobox(self):
        positions = [pos[1] for pos in self.position]
        self.ui.position_combobox.addItems(positions)


class AddScheduleWindow(QtWidgets.QMainWindow):
    """ Add new row into schedule table """
    def __init__(self, salary):
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

        self.tab_to_window = [AddEmployeeWindow, AddScheduleWindow]

        self.ui.tabBar.setCurrentIndex(0)
        self.salary.show_table(0)

        self.ui.tabBar.currentChanged.connect(self.tab_changed)
        self.ui.addButton.clicked.connect(self.open_window)
        self.ui.delButton.clicked.connect(self.delete_selected_row)

    def tab_changed(self):
        tab_index = self.ui.tabBar.currentIndex()
        self.salary.show_table(tab_index)

    def open_window(self):
        tab_index = self.ui.tabBar.currentIndex()
        self.window = self.tab_to_window[tab_index](self.salary)
        self.window.show()

    def delete_selected_row(self):
        tab_index = self.ui.tabBar.currentIndex()
        self.salary.delete_row(tab_index)


def main():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
