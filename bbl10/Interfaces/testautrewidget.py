# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testautrewidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 558)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setObjectName("widget")
        self.timeEdit = QtWidgets.QTimeEdit(self.widget2)
        self.timeEdit.setGeometry(QtCore.QRect(200, 170, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.widget2)
        self.dateEdit.setGeometry(QtCore.QRect(50, 310, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.widget2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
