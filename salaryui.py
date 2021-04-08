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
            'empTab': ui.employeestable,
            'schtab': ui.scheduletable,
            'payTab': ui.posTab
        }

    def show_table(self, table_name, ui_tab_table):
        table_data = self.get_table(table_name)
        table_shape = table_data[0]
        table = table_data[1]


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setFont(QtGui.QFont('Times'))

        salary = SalaryGui({
                'host': 'localhost',
                'user': 'root',
                'password': os.environ.get('SQL_CONNECTOR_PASS'),
                'database': 'salary_calc'}
        )

        table = salary.get_table('position')
        position_shape = table[0]
        self.ui.comboBox.addItems(salary.get_position_list())
        self.ui.tableWidget.setColumnCount(position_shape[1])
        self.ui.tableWidget.setRowCount(position_shape[0])
        position_table = table[1]
        for row, tup in enumerate(position_table):
            for col, item in enumerate(tup):
                cell_value = QtWidgets.QTableWidgetItem(str(item))
                cell_value.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row, col, cell_value)


def main():
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
