# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_window(object):
    def setupUi(self, add_window):
        add_window.setObjectName("add_window")
        add_window.resize(252, 141)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(add_window.sizePolicy().hasHeightForWidth())
        add_window.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(add_window)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(add_window)
        self.stackedWidget.setObjectName("stackedWidget")
        self.add_employee = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_employee.sizePolicy().hasHeightForWidth())
        self.add_employee.setSizePolicy(sizePolicy)
        self.add_employee.setObjectName("add_employee")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.add_employee)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.employee_fields = QtWidgets.QFormLayout()
        self.employee_fields.setObjectName("employee_fields")
        self.emp_name_label = QtWidgets.QLabel(self.add_employee)
        self.emp_name_label.setObjectName("emp_name_label")
        self.employee_fields.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.emp_name_label)
        self.emp_name_line = QtWidgets.QLineEdit(self.add_employee)
        self.emp_name_line.setObjectName("emp_name_line")
        self.employee_fields.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.emp_name_line)
        self.pos_label = QtWidgets.QLabel(self.add_employee)
        self.pos_label.setObjectName("pos_label")
        self.employee_fields.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pos_label)
        self.pos_cb = QtWidgets.QComboBox(self.add_employee)
        self.pos_cb.setObjectName("pos_cb")
        self.employee_fields.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pos_cb)
        self.gridLayout_4.addLayout(self.employee_fields, 0, 0, 1, 1)
        self.employee_buttons = QtWidgets.QHBoxLayout()
        self.employee_buttons.setObjectName("employee_buttons")
        self.emp_add_button = QtWidgets.QPushButton(self.add_employee)
        self.emp_add_button.setObjectName("emp_add_button")
        self.employee_buttons.addWidget(self.emp_add_button)
        self.emp_cancel_button = QtWidgets.QPushButton(self.add_employee)
        self.emp_cancel_button.setObjectName("emp_cancel_button")
        self.employee_buttons.addWidget(self.emp_cancel_button)
        self.gridLayout_4.addLayout(self.employee_buttons, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.add_employee)
        self.add_schedule = QtWidgets.QWidget()
        self.add_schedule.setObjectName("add_schedule")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.add_schedule)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.schedule_fields = QtWidgets.QFormLayout()
        self.schedule_fields.setObjectName("schedule_fields")
        self.sch_emp_label = QtWidgets.QLabel(self.add_schedule)
        self.sch_emp_label.setObjectName("sch_emp_label")
        self.schedule_fields.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sch_emp_label)
        self.sch_hrs_label = QtWidgets.QLabel(self.add_schedule)
        self.sch_hrs_label.setObjectName("sch_hrs_label")
        self.schedule_fields.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sch_hrs_label)
        self.csh_date_label = QtWidgets.QLabel(self.add_schedule)
        self.csh_date_label.setObjectName("csh_date_label")
        self.schedule_fields.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.csh_date_label)
        self.sch_date_edit = QtWidgets.QDateEdit(self.add_schedule)
        self.sch_date_edit.setCalendarPopup(True)
        self.sch_date_edit.setObjectName("sch_date_edit")
        self.schedule_fields.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sch_date_edit)
        self.sch_emp_cb = QtWidgets.QComboBox(self.add_schedule)
        self.sch_emp_cb.setObjectName("sch_emp_cb")
        self.schedule_fields.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sch_emp_cb)
        self.sch_hrs_box = QtWidgets.QSpinBox(self.add_schedule)
        self.sch_hrs_box.setMaximum(24)
        self.sch_hrs_box.setObjectName("sch_hrs_box")
        self.schedule_fields.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sch_hrs_box)
        self.gridLayout_5.addLayout(self.schedule_fields, 0, 0, 1, 1)
        self.schedule_buttons = QtWidgets.QHBoxLayout()
        self.schedule_buttons.setObjectName("schedule_buttons")
        self.sch_add_button = QtWidgets.QPushButton(self.add_schedule)
        self.sch_add_button.setObjectName("sch_add_button")
        self.schedule_buttons.addWidget(self.sch_add_button)
        self.sch_cancel_button = QtWidgets.QPushButton(self.add_schedule)
        self.sch_cancel_button.setObjectName("sch_cancel_button")
        self.schedule_buttons.addWidget(self.sch_cancel_button)
        self.gridLayout_5.addLayout(self.schedule_buttons, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.add_schedule)
        self.add_payment = QtWidgets.QWidget()
        self.add_payment.setObjectName("add_payment")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.add_payment)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.payment_fields = QtWidgets.QFormLayout()
        self.payment_fields.setObjectName("payment_fields")
        self.pay_emp_label = QtWidgets.QLabel(self.add_payment)
        self.pay_emp_label.setObjectName("pay_emp_label")
        self.payment_fields.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pay_emp_label)
        self.pay_date_label = QtWidgets.QLabel(self.add_payment)
        self.pay_date_label.setObjectName("pay_date_label")
        self.payment_fields.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pay_date_label)
        self.pay_date_edit = QtWidgets.QDateEdit(self.add_payment)
        self.pay_date_edit.setObjectName("pay_date_edit")
        self.payment_fields.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pay_date_edit)
        self.pay_nomhrs_label = QtWidgets.QLabel(self.add_payment)
        self.pay_nomhrs_label.setObjectName("pay_nomhrs_label")
        self.payment_fields.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pay_nomhrs_label)
        self.pay_nomhrs_box = QtWidgets.QSpinBox(self.add_payment)
        self.pay_nomhrs_box.setObjectName("pay_nomhrs_box")
        self.payment_fields.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pay_nomhrs_box)
        self.pay_emp_cb = QtWidgets.QComboBox(self.add_payment)
        self.pay_emp_cb.setObjectName("pay_emp_cb")
        self.payment_fields.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pay_emp_cb)
        self.gridLayout_3.addLayout(self.payment_fields, 0, 0, 1, 1)
        self.payment_buttons = QtWidgets.QHBoxLayout()
        self.payment_buttons.setObjectName("payment_buttons")
        self.pay_add_button = QtWidgets.QPushButton(self.add_payment)
        self.pay_add_button.setObjectName("pay_add_button")
        self.payment_buttons.addWidget(self.pay_add_button)
        self.pay_cancel_button = QtWidgets.QPushButton(self.add_payment)
        self.pay_cancel_button.setObjectName("pay_cancel_button")
        self.payment_buttons.addWidget(self.pay_cancel_button)
        self.gridLayout_3.addLayout(self.payment_buttons, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.add_payment)
        self.add_position = QtWidgets.QWidget()
        self.add_position.setObjectName("add_position")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.add_position)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.position_fields = QtWidgets.QFormLayout()
        self.position_fields.setObjectName("position_fields")
        self.pos_title_label = QtWidgets.QLabel(self.add_position)
        self.pos_title_label.setObjectName("pos_title_label")
        self.position_fields.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pos_title_label)
        self.pos_title_line = QtWidgets.QLineEdit(self.add_position)
        self.pos_title_line.setObjectName("pos_title_line")
        self.position_fields.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pos_title_line)
        self.pos_rate_label = QtWidgets.QLabel(self.add_position)
        self.pos_rate_label.setObjectName("pos_rate_label")
        self.position_fields.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pos_rate_label)
        self.pos_rate_box = QtWidgets.QSpinBox(self.add_position)
        self.pos_rate_box.setObjectName("pos_rate_box")
        self.position_fields.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pos_rate_box)
        self.gridLayout_6.addLayout(self.position_fields, 0, 0, 1, 1)
        self.position_buttons = QtWidgets.QHBoxLayout()
        self.position_buttons.setObjectName("position_buttons")
        self.pos_add_button = QtWidgets.QPushButton(self.add_position)
        self.pos_add_button.setObjectName("pos_add_button")
        self.position_buttons.addWidget(self.pos_add_button)
        self.pos_cancel_button = QtWidgets.QPushButton(self.add_position)
        self.pos_cancel_button.setObjectName("pos_cancel_button")
        self.position_buttons.addWidget(self.pos_cancel_button)
        self.gridLayout_6.addLayout(self.position_buttons, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.add_position)
        self.add_paystatus = QtWidgets.QWidget()
        self.add_paystatus.setObjectName("add_paystatus")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.add_paystatus)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.paystatus_fields = QtWidgets.QFormLayout()
        self.paystatus_fields.setObjectName("paystatus_fields")
        self.paystatus_title_label = QtWidgets.QLabel(self.add_paystatus)
        self.paystatus_title_label.setObjectName("paystatus_title_label")
        self.paystatus_fields.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.paystatus_title_label)
        self.paystatus_title_line = QtWidgets.QLineEdit(self.add_paystatus)
        self.paystatus_title_line.setObjectName("paystatus_title_line")
        self.paystatus_fields.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.paystatus_title_line)
        self.paystatus_rate_label = QtWidgets.QLabel(self.add_paystatus)
        self.paystatus_rate_label.setObjectName("paystatus_rate_label")
        self.paystatus_fields.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.paystatus_rate_label)
        self.paystatus_rate_box = QtWidgets.QSpinBox(self.add_paystatus)
        self.paystatus_rate_box.setObjectName("paystatus_rate_box")
        self.paystatus_fields.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.paystatus_rate_box)
        self.gridLayout_7.addLayout(self.paystatus_fields, 0, 0, 1, 1)
        self.paystatus_buttons = QtWidgets.QHBoxLayout()
        self.paystatus_buttons.setObjectName("paystatus_buttons")
        self.paystatus_add_button = QtWidgets.QPushButton(self.add_paystatus)
        self.paystatus_add_button.setObjectName("paystatus_add_button")
        self.paystatus_buttons.addWidget(self.paystatus_add_button)
        self.paystatus_cancel_button = QtWidgets.QPushButton(self.add_paystatus)
        self.paystatus_cancel_button.setObjectName("paystatus_cancel_button")
        self.paystatus_buttons.addWidget(self.paystatus_cancel_button)
        self.gridLayout_7.addLayout(self.paystatus_buttons, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.add_paystatus)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.retranslateUi(add_window)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(add_window)

    def retranslateUi(self, add_window):
        _translate = QtCore.QCoreApplication.translate
        add_window.setWindowTitle(_translate("add_window", "Add"))
        self.emp_name_label.setText(_translate("add_window", "Employee name"))
        self.pos_label.setText(_translate("add_window", "Position"))
        self.emp_add_button.setText(_translate("add_window", "Add"))
        self.emp_cancel_button.setText(_translate("add_window", "Cancel"))
        self.sch_emp_label.setText(_translate("add_window", "Employee"))
        self.sch_hrs_label.setText(_translate("add_window", "Hours"))
        self.csh_date_label.setText(_translate("add_window", "Date"))
        self.sch_add_button.setText(_translate("add_window", "Add"))
        self.sch_cancel_button.setText(_translate("add_window", "Cancel"))
        self.pay_emp_label.setText(_translate("add_window", "Employee"))
        self.pay_date_label.setText(_translate("add_window", "Date"))
        self.pay_nomhrs_label.setText(_translate("add_window", "Nominal hours"))
        self.pay_add_button.setText(_translate("add_window", "Add"))
        self.pay_cancel_button.setText(_translate("add_window", "Cancel"))
        self.pos_title_label.setText(_translate("add_window", "Title"))
        self.pos_rate_label.setText(_translate("add_window", "Rate"))
        self.pos_add_button.setText(_translate("add_window", "Add"))
        self.pos_cancel_button.setText(_translate("add_window", "Cancel"))
        self.paystatus_title_label.setText(_translate("add_window", "Title"))
        self.paystatus_rate_label.setText(_translate("add_window", "Rate"))
        self.paystatus_add_button.setText(_translate("add_window", "Add"))
        self.paystatus_cancel_button.setText(_translate("add_window", "Cancel"))
