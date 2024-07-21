# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QLabel, QVBoxLayout,QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
import os,json,glob


'''

"scrn1": [
    "MS Mincho",
    40
],
"scrn2": [
    "Papyrus",
    46,
    "nature2"
],
"scrn2_baiboly": [
    40,
    200
],
"scrn2_label_size": [
    1300,
    680
]
'''

content=dict()
current_link=os.getcwd()
image_path__=f"{current_link}//files//images//image_sombre.jpg"
chm_baiboly=f"{current_link}//files//DB//baiboly"
chm_fihirana=f"{current_link}//files//DB//fihirana"
chm_json_scrn1=f"{current_link}//files//dependances//scrn1_out.json"

class Parametre_App(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(388, 525)
        self.setMinimumSize(QtCore.QSize(298, 525))
        self.setMaximumSize(QtCore.QSize(388, 525))
        self.gridLayout_3 = QtWidgets.QGridLayout(self)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.fontComboBox_1scren = QtWidgets.QFontComboBox(self.groupBox)
        self.fontComboBox_1scren.setObjectName("fontComboBox_1scren")
        self.horizontalLayout.addWidget(self.fontComboBox_1scren)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox1scrn = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox1scrn.setObjectName("spinBox1scrn")
        self.horizontalLayout_2.addWidget(self.spinBox1scrn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.fontComboBox_2scrn = QtWidgets.QFontComboBox(self.groupBox_2)
        self.fontComboBox_2scrn.setObjectName("fontComboBox_2scrn")
        self.horizontalLayout_3.addWidget(self.fontComboBox_2scrn)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spinBox_2scrn = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2scrn.setObjectName("spinBox_2scrn")
        self.horizontalLayout_4.addWidget(self.spinBox_2scrn)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.comboBox_2scrn = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2scrn.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_2scrn.setObjectName("comboBox_2scrn")
        self.horizontalLayout_6.addWidget(self.comboBox_2scrn)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.spinBox_largeur_label2nd = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_largeur_label2nd.setObjectName("spinBox_largeur_label2nd")
        self.horizontalLayout_8.addWidget(self.spinBox_largeur_label2nd)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.spinBox_hauteur_label2nd = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_hauteur_label2nd.setObjectName("spinBox_hauteur_label2nd")
        self.horizontalLayout_9.addWidget(self.spinBox_hauteur_label2nd)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setMinimumSize(QtCore.QSize(100, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.spinBox_2scrn_2 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_2scrn_2.setObjectName("spinBox_2scrn_2")
        self.horizontalLayout_7.addWidget(self.spinBox_2scrn_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spinBox_2scrn_3 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_2scrn_3.setObjectName("spinBox_2scrn_3")
        self.horizontalLayout_5.addWidget(self.spinBox_2scrn_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sauvegarde = QtWidgets.QPushButton(self.tab)
        self.sauvegarde.setObjectName("sauvegarde")
        self.verticalLayout_2.addWidget(self.sauvegarde)
        self.reinitialiser_parametre = QtWidgets.QPushButton(self.tab)
        self.reinitialiser_parametre.setObjectName("reinitialiser_parametre")
        self.verticalLayout_2.addWidget(self.reinitialiser_parametre)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.spinBox_lum_img = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_lum_img.setObjectName("spinBox_lum_img")
        self.horizontalLayout_10.addWidget(self.spinBox_lum_img)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.tabWidget.setCurrentIndex(0)

        
        self.spinBox1scrn.setMaximum(10000)
        #self.spinBox_2scrn.setMaximum(10000)
        self.spinBox_2scrn_2.setMaximum(10000)
        self.spinBox_2scrn_3.setMaximum(10000)
        self.spinBox_hauteur_label2nd.setMaximum(10000)
        self.spinBox_largeur_label2nd.setMaximum(10000)
        
        self.setWindowTitle("Paramêtre")
        self.groupBox.setTitle("1er Ecran")
        self.label.setText("Police :")
        self.label_2.setText("Size text label :")
        self.groupBox_2.setTitle("2ème écran")
        self.label_3.setText("Police :")
        self.label_4.setText("Size text label :")
        self.label_6.setText("Image font :")
        self.groupBox_4.setTitle("Taille du label")
        self.label_8.setText("Largeur :")
        self.label_9.setText("Hauteur :")
        self.groupBox_3.setTitle("Baiboly")
        self.label_7.setText("Ligne nombre de mot :")
        self.label_5.setText("Sequence nbr mot :")
        self.sauvegarde.setText("Sauvegarde")
        self.reinitialiser_parametre.setText("Reinitialiser parametre")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Paramètre Général")
        self.groupBox_5.setTitle("Parametre image de fond")
        self.label_10.setText("Luminosité de l\'image :")
        self.pushButton.setText("Appliquer modification")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Modifier image")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "Mis à jour des données")

        self.sauvegarde.setShortcut('s')

        self.comboBox_2scrn.clear()
        new_option = ['nature','nature2']
        self.comboBox_2scrn.addItems(new_option)
        self.reinitialiser_parametre.clicked.connect(self.dt_innit)
        self.sauvegarde.clicked.connect(self.save)
        self.prnt_data()

    
    def prnt_data(self):
        with open(f"{current_link}\\files//dependances//param.json", "r",encoding='utf-8') as f:
            dt=json.load(f)
            
        scrn1=dt['scrn1']
        self.fontComboBox_1scren.setCurrentFont(QFont(scrn1[0]))
        self.spinBox1scrn.setValue(scrn1[1])
        
        scrn2=dt['scrn2']
        self.fontComboBox_2scrn.setCurrentFont(QFont(scrn2[0]))
        self.spinBox_2scrn.setValue(scrn2[1])
        self.comboBox_2scrn.setCurrentText(scrn2[2])
        
        scrn2_baiboly=dt['scrn2_baiboly']
        self.spinBox_2scrn_2.setValue(scrn2_baiboly[0])
        self.spinBox_2scrn_3.setValue(scrn2_baiboly[1])

        scrn2_label_size=dt['scrn2_label_size']
        self.spinBox_largeur_label2nd.setValue(scrn2_label_size[0])
        self.spinBox_hauteur_label2nd.setValue(scrn2_label_size[1])

    def show_confirmation_dialog(self,message):
        reply = QMessageBox.question(None, 'Confirmation', message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        return reply == QMessageBox.Yes

    def dt_innit(self):
        if self.show_confirmation_dialog('Voulez-vous vraiment réinitialiser les paramètres'):
            with open(f"{current_link}\\files//dependances//innit_param.json", "r",encoding='utf-8') as f:
                dt__innit__=json.load(f)
                
            with open(f"{current_link}\\files//dependances//param.json", "w",encoding='utf-8') as f:
                json.dump(dt__innit__,f,indent=4, ensure_ascii= False, sort_keys=False)
            
            self.prnt_data()
            print('Paramètre Réinitialiser')
            
        else:
            pass
    
    def save(self):
        scrn1_font=self.fontComboBox_1scren.currentFont()
        scrn1_sizetext=self.spinBox1scrn.value()
        content['scrn1']=scrn1_font.family(),scrn1_sizetext

        scrn2_font=self.fontComboBox_2scrn.currentFont()
        scrn2_sizetext=self.spinBox_2scrn.value()
        scrn2_image_font=self.comboBox_2scrn.currentText()
        content['scrn2']=scrn2_font.family(),scrn2_sizetext,scrn2_image_font

        scrn2_baiboly_nbr_mot_ligne=self.spinBox_2scrn_2.value()
        scrn2_baiboly_nbr_mot_sequence=self.spinBox_2scrn_3.value()
        content['scrn2_baiboly']=scrn2_baiboly_nbr_mot_ligne,scrn2_baiboly_nbr_mot_sequence

        content['scrn2_label_size']=int(self.spinBox_largeur_label2nd.value()),int(self.spinBox_hauteur_label2nd.value())

        with open(f"{current_link}\\files//dependances//param.json", "w",encoding='utf-8') as f:
            json.dump(content,f,indent=4, ensure_ascii= False, sort_keys=False)
        print(f'saved')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Parametre = Parametre_App()
    Parametre.show()
    sys.exit(app.exec_())