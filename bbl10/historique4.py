# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QLabel, QVBoxLayout,QPushButton, QMessageBox

class Historique_App(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.setMinimumSize(QtCore.QSize(600, 300))
        self.setMaximumSize(QtCore.QSize(600, 300))
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_years = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_years.setMinimumSize(QtCore.QSize(80, 0))
        self.comboBox_years.setObjectName("comboBox_years")
        self.comboBox_years.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_years)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.comboBox_month = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_month.setMinimumSize(QtCore.QSize(90, 0))
        self.comboBox_month.setObjectName("comboBox_month")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_month)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.comboBox_day = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_day.setMinimumSize(QtCore.QSize(90, 0))
        self.comboBox_day.setObjectName("comboBox_day")
        self.comboBox_day.addItem("")
        self.comboBox_day.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_day)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_7.addWidget(self.line_3)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.setWindowTitle("Historique")
        self.groupBox.setTitle("Filtrer Historique")
        self.label.setText("Année :")
        self.comboBox_years.setItemText(0, "2023")
        self.label_2.setText("Mois :")
        self.comboBox_month.setItemText(0, "All")
        self.comboBox_month.setItemText(1, "Décembre")
        self.label_3.setText("Jour :")
        self.comboBox_day.setItemText(0, "All")
        self.comboBox_day.setItemText(1, "Samedi")
        self.pushButton.setText("Exporter")
        self.plainTextEdit.setPlainText("")


    def comb_years(self,dt):
        self.comboBox_years.clear()
        new_option = dt
        self.comboBox_years.addItems(new_option)
"""
"2023 Oct 21 (Sat):\n"
" Baiboly:\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
" Fihirana:\n"
"  2 MISAOTRA RY TOMPO ANDRIAMANITRA(22:38:03)\n"
"  2 MISAOTRA RY TOMPO ANDRIAMANITRA(22:38:03)\n"
"  2 MISAOTRA RY TOMPO ANDRIAMANITRA(22:38:03)\n"
"\n"
"2023 Oct 21 (Sat):\n"
" Baiboly:\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
"  Efesiana 6 : 15 (15:50:57)\n"
" Fihirana:\n"
"  2 MISAOTRA RY TOMPO ANDRIAMANITRA(22:38:03)\n"
"  2 MISAOTRA RY TOMPO ANDRIAMANITRA(22:38:03)\n"
"  2 MISAOTRA RY TOMPO ANDRIAMANITRA(22:38:03)\n"
"""

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Historique = Historique_App()
    Historique.show()
    sys.exit(app.exec_())