# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import os,sqlite3,textwrap,json
from add_fonction2 import baiboly_G, fihirana_G
from PyQt5.QtGui import QIcon
from bbl1_5_2_6 import MyWidget

from historique4 import Historique_App
from parametre2_1 import Parametre_App
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QScreen

current_link=os.getcwd()
connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
curseur = connexion.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1648, 586)
        #icon=QIcon("book_.png")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{current_link}//files//images//book_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1603, 634))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("MS Mincho")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.Baiboly = QtWidgets.QTabWidget(self.centralwidget)
        self.Baiboly.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Baiboly.setFont(font)
        self.Baiboly.setObjectName("Baiboly")
        self.Baiboly_2 = QtWidgets.QWidget()
        self.Baiboly_2.setObjectName("Baiboly_2")
        self.gridLayout = QtWidgets.QGridLayout(self.Baiboly_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.conf_view = QtWidgets.QLabel(self.Baiboly_2)
        self.conf_view.setMinimumSize(QtCore.QSize(250, 0))
        self.conf_view.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.conf_view.setFont(font)
        self.conf_view.setAlignment(QtCore.Qt.AlignCenter)
        self.conf_view.setObjectName("conf_view")
        self.horizontalLayout.addWidget(self.conf_view)
        self.checkBox_Signaler_baiboly = QtWidgets.QCheckBox(self.Baiboly_2)
        self.checkBox_Signaler_baiboly.setMaximumSize(QtCore.QSize(250, 16777215))
        self.checkBox_Signaler_baiboly.setObjectName("checkBox_Signaler_baiboly")
        self.horizontalLayout.addWidget(self.checkBox_Signaler_baiboly)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_testameta1 = QtWidgets.QRadioButton(self.Baiboly_2)
        self.radioButton_testameta1.setObjectName("radioButton_testameta1")
        self.horizontalLayout_6.addWidget(self.radioButton_testameta1)
        self.radioButton_testameta2 = QtWidgets.QRadioButton(self.Baiboly_2)
        self.radioButton_testameta2.setObjectName("radioButton_testameta2")
        self.horizontalLayout_6.addWidget(self.radioButton_testameta2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.label_2 = QtWidgets.QLabel(self.Baiboly_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.comboBox_boky = QtWidgets.QComboBox(self.Baiboly_2)
        self.comboBox_boky.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_boky.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_boky.setObjectName("comboBox_boky")
        self.comboBox_boky.addItem("")
        self.comboBox_boky.setItemText(0, "")
        self.comboBox_boky.addItem("")
        self.comboBox_boky.addItem("")
        self.comboBox_boky.addItem("")
        self.comboBox_boky.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_boky)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_toko = QtWidgets.QLabel(self.Baiboly_2)
        self.label_toko.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_toko.setFont(font)
        self.label_toko.setObjectName("label_toko")
        self.horizontalLayout_4.addWidget(self.label_toko)
        self.toko = QtWidgets.QLineEdit(self.Baiboly_2)
        self.toko.setMaximumSize(QtCore.QSize(50, 16777215))
        self.toko.setAlignment(QtCore.Qt.AlignCenter)
        self.toko.setObjectName("toko")
        self.horizontalLayout_4.addWidget(self.toko)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_andininy = QtWidgets.QLabel(self.Baiboly_2)
        self.label_andininy.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_andininy.setFont(font)
        self.label_andininy.setObjectName("label_andininy")
        self.horizontalLayout_5.addWidget(self.label_andininy)
        self.andininy = QtWidgets.QLineEdit(self.Baiboly_2)
        self.andininy.setMaximumSize(QtCore.QSize(150, 16777215))
        self.andininy.setAlignment(QtCore.Qt.AlignCenter)
        self.andininy.setObjectName("andininy")
        self.horizontalLayout_5.addWidget(self.andininy)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.Baiboly.addTab(self.Baiboly_2, "")
        self.fihirana = QtWidgets.QWidget()
        self.fihirana.setObjectName("fihirana")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.fihirana)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.conf_view_2 = QtWidgets.QLabel(self.fihirana)
        self.conf_view_2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.conf_view_2.setFont(font)
        self.conf_view_2.setAlignment(QtCore.Qt.AlignCenter)
        self.conf_view_2.setObjectName("conf_view_2")
        self.horizontalLayout_2.addWidget(self.conf_view_2)
        self.checkBoxSignaler_fihirana = QtWidgets.QCheckBox(self.fihirana)
        self.checkBoxSignaler_fihirana.setMaximumSize(QtCore.QSize(250, 16777215))
        self.checkBoxSignaler_fihirana.setObjectName("checkBoxSignaler_fihirana")
        self.horizontalLayout_2.addWidget(self.checkBoxSignaler_fihirana)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.radioButton_fihirana1 = QtWidgets.QRadioButton(self.fihirana)
        self.radioButton_fihirana1.setObjectName("radioButton_fihirana1")
        self.horizontalLayout_18.addWidget(self.radioButton_fihirana1)
        self.radioButton_fihirana2 = QtWidgets.QRadioButton(self.fihirana)
        self.radioButton_fihirana2.setObjectName("radioButton_fihirana2")
        self.horizontalLayout_18.addWidget(self.radioButton_fihirana2)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.line = QtWidgets.QFrame(self.fihirana)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_21.addWidget(self.line)
        self.line_2 = QtWidgets.QFrame(self.fihirana)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_21.addWidget(self.line_2)
        self.label_16 = QtWidgets.QLabel(self.fihirana)
        self.label_16.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_21.addWidget(self.label_16)
        self.fihirana_laharana = QtWidgets.QLineEdit(self.fihirana)
        self.fihirana_laharana.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fihirana_laharana.setAlignment(QtCore.Qt.AlignCenter)
        self.fihirana_laharana.setObjectName("fihirana_laharana")
        self.horizontalLayout_21.addWidget(self.fihirana_laharana)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_14 = QtWidgets.QLabel(self.fihirana)
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_19.addWidget(self.label_14)
        self.lohateny = QtWidgets.QLineEdit(self.fihirana)
        self.lohateny.setMinimumSize(QtCore.QSize(350, 0))
        self.lohateny.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lohateny.setAlignment(QtCore.Qt.AlignCenter)
        self.lohateny.setObjectName("lohateny")
        self.horizontalLayout_19.addWidget(self.lohateny)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_15 = QtWidgets.QLabel(self.fihirana)
        self.label_15.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_20.addWidget(self.label_15)
        self.cles = QtWidgets.QLineEdit(self.fihirana)
        self.cles.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cles.setAlignment(QtCore.Qt.AlignCenter)
        self.cles.setObjectName("cles")
        self.horizontalLayout_20.addWidget(self.cles)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_20)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)
        self.Baiboly.addTab(self.fihirana, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.checkBoxSignaler_fihiranaFanampiny = QtWidgets.QCheckBox(self.tab)
        self.checkBoxSignaler_fihiranaFanampiny.setMaximumSize(QtCore.QSize(250, 16777215))
        self.checkBoxSignaler_fihiranaFanampiny.setObjectName("checkBoxSignaler_fihiranaFanampiny")
        self.horizontalLayout_8.addWidget(self.checkBoxSignaler_fihiranaFanampiny)
        self.gridLayout_5.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_lohateny = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_lohateny.setMinimumSize(QtCore.QSize(1250, 0))
        self.lineEdit_lohateny.setMaximumSize(QtCore.QSize(1250, 16777215))
        self.lineEdit_lohateny.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_lohateny.setReadOnly(False)
        self.lineEdit_lohateny.setObjectName("lineEdit_lohateny")
        self.horizontalLayout_3.addWidget(self.lineEdit_lohateny)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.Baiboly.addTab(self.tab, "")
        self.gridLayout_3.addWidget(self.Baiboly, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1648, 26))
        self.menubar.setObjectName("menubar")
        self.menuOutils = QtWidgets.QMenu(self.menubar)
        self.menuOutils.setObjectName("menuOutils")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHistorique = QtWidgets.QAction(MainWindow)
        self.actionHistorique.setObjectName("actionHistorique")
        self.actionMode_2_me_cran = QtWidgets.QAction(MainWindow)
        self.actionMode_2_me_cran.setObjectName("actionMode_2_me_cran")
        self.actionPartition = QtWidgets.QAction(MainWindow)
        self.actionPartition.setObjectName("actionPartition")
        self.actionPolice = QtWidgets.QAction(MainWindow)
        self.actionPolice.setObjectName("actionPolice")
        self.actionImage_de_fond = QtWidgets.QAction(MainWindow)
        self.actionImage_de_fond.setObjectName("actionImage_de_fond")
        self.actionParam_tre_General = QtWidgets.QAction(MainWindow)
        self.actionParam_tre_General.setObjectName("actionParam_tre_General")
        self.actionParam_tre_G_n_ral = QtWidgets.QAction(MainWindow)
        self.actionParam_tre_G_n_ral.setObjectName("actionParam_tre_G_n_ral")
        self.actionParametre = QtWidgets.QAction(MainWindow)
        self.actionParametre.setObjectName("actionParametre")
        self.menuOutils.addAction(self.actionHistorique)
        self.menuOutils.addAction(self.actionMode_2_me_cran)
        self.menuOutils.addAction(self.actionPartition)
        self.menuOutils.addSeparator()
        self.menuOutils.addAction(self.actionParametre)
        self.menubar.addAction(self.menuOutils.menuAction())
        
        self.label.setWordWrap(True)
        self.label.setMargin(100)

        self.retranslateUi(MainWindow)
        self.Baiboly.setCurrentIndex(0)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.second_fenetre_ouverte = False
        self.ecran__2 = None
        self.contentLabel=[]
        
        self.comboBox_boky.currentIndexChanged.connect(self.chptr)
        self.toko.editingFinished.connect(self.vrst)
        self.andininy.editingFinished.connect(self.diffusion_btn)
        self.fihirana_laharana.textChanged.connect(self.ffint)
        self.lineEdit_lohateny.textChanged.connect(self.fihirana_f)
        self.lineEdit_lohateny.editingFinished.connect(self.fihirana_content)
        #self.andininy.editingFinished.connect(self.vrst2)
        self.Baiboly.currentChanged.connect(self.on_tab_clik) # type: ignore
        self.radioButton_testameta1.clicked.connect(self.testmnt1) # type: ignore
        self.radioButton_testameta2.clicked.connect(self.testmnt2) # type: ignore

        self.radioButton_testameta1.setChecked(True)
        self.testmnt1()
        #self.radioButton_fihirana1
        #self.btn_view.clicked.connect(self.diffusion_btn) # type: ignore
        #self.btn_view_2.clicked.connect(self.read_fihirana)
        
        self.actionMode_2_me_cran.triggered.connect(self.ecran_2)
        self.actionParametre.triggered.connect(self.param)
        self.actionHistorique.triggered.connect(self.historique)
        
        #self.radioButton_fihirana1.clicked.connect(self.fihirana1)
        #self.radioButton_fihirana2.clicked.connect(self.fihirana2)

        #self.second_interface=MyWidget()
        
        #Les raccourci
        self.actionMode_2_me_cran.setShortcut('e')
        self.actionHistorique.setShortcut('h')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BAIBOLY"))
        self.conf_view.setText(_translate("MainWindow", "--"))
        self.checkBox_Signaler_baiboly.setText(_translate("MainWindow", "Signaler"))
        self.radioButton_testameta1.setText(_translate("MainWindow", "Testameta Voalohany"))
        self.radioButton_testameta2.setText(_translate("MainWindow", "Testameta Faharoa"))
        self.label_2.setText(_translate("MainWindow", "Boky :"))
        self.comboBox_boky.setItemText(1, _translate("MainWindow", "Genesisy"))
        self.comboBox_boky.setItemText(2, _translate("MainWindow", "Eksodosy"))
        self.comboBox_boky.setItemText(3, _translate("MainWindow", "Levitikosy"))
        self.comboBox_boky.setItemText(4, _translate("MainWindow", "Nomeria"))
        self.label_toko.setText(_translate("MainWindow", "Toko :"))
        self.label_andininy.setText(_translate("MainWindow", "Andininy :"))
        self.Baiboly.setTabText(self.Baiboly.indexOf(self.Baiboly_2), _translate("MainWindow", "Baiboly"))
        self.conf_view_2.setText(_translate("MainWindow", "--"))
        self.checkBoxSignaler_fihirana.setText(_translate("MainWindow", "Signaler"))
        self.radioButton_fihirana1.setText(_translate("MainWindow", "Fihirana Voalohany"))
        self.radioButton_fihirana2.setText(_translate("MainWindow", "Fihirana Faharoa"))
        self.label_16.setText(_translate("MainWindow", "Laharana :"))
        self.label_14.setText(_translate("MainWindow", "Lohateny:"))
        self.label_15.setText(_translate("MainWindow", "Clés :"))
        self.Baiboly.setTabText(self.Baiboly.indexOf(self.fihirana), _translate("MainWindow", "Fihirana"))
        self.label_4.setText(_translate("MainWindow", "TextLabel3"))
        self.checkBoxSignaler_fihiranaFanampiny.setText(_translate("MainWindow", "Signaler"))
        self.label_3.setText(_translate("MainWindow", "LOHATENY: "))
        self.Baiboly.setTabText(self.Baiboly.indexOf(self.tab), _translate("MainWindow", "Fihirana fanampiny"))
        self.menuOutils.setTitle(_translate("MainWindow", "Outils"))
        self.actionHistorique.setText(_translate("MainWindow", "Historique"))
        self.actionMode_2_me_cran.setText(_translate("MainWindow", "Mode 2ème écran"))
        self.actionPartition.setText(_translate("MainWindow", "Liste hira"))
        self.actionPolice.setText(_translate("MainWindow", "Police"))
        self.actionImage_de_fond.setText(_translate("MainWindow", "Image de fond"))
        self.actionParam_tre_General.setText(_translate("MainWindow", "Paramètre General"))
        self.actionParam_tre_G_n_ral.setText(_translate("MainWindow", "Paramètre Général"))
        self.actionParametre.setText(_translate("MainWindow", "Parametre Général"))
        

    def mod_text(self):
        if self.Baiboly.currentIndex()==0:
            boky=self.comboBox_boky.currentText()
            begning =self.andininy.text()
            conf = f"{boky} {self.toko.text()} : {begning}"
            
            if boky  and (self.toko.text())=="":
                pass
            else:
                bbl=baiboly_G.baiboly(conf)

                phrases='\n'.join(bbl)
                mots=phrases.split()
                #print(mots)
                with open(f"{current_link}\\files//dependances//param.json", "r",encoding='utf-8') as f:
                    dt=json.load(f)
                lgn=dt['scrn1']
                bbl_cntt=dt['scrn2_baiboly']

                #print(type(bbl_cntt[1]))

                max_caracteres_par_ligne_1 = int(lgn[1])
                max_caracteres_par_ligne_2 = 35

                texte_modifie_1 = textwrap.fill("\n".join(mots), width=max_caracteres_par_ligne_1)
                
                #print(texte_modifie_1)
                texte_modifie_1_= textwrap.wrap(texte_modifie_1,width=300)
                #print(texte_modifie_1_)
                
                texte_modifie_2 =textwrap.wrap(phrases, width=int(bbl_cntt[1]))
                #print(type(texte_modifie_2))

                #texte_modifie_2 = textwrap.fill("\n".join(mots), width=max_caracteres_par_ligne_2)
            
            return conf,texte_modifie_1_,texte_modifie_2,'bbl'
        '''else:
            if self.radioButton_fihirana1.isChecked():
                fh_1=self.fihirana_laharana.text()
                fh_2=self.lohateny.text()            
                conf=f" {(fh_2).upper()} "
                fhn=fihirana_G.fihirana1(fh_1,(fh_2).upper())
                #fhn2=fihirana_G.fihirana1_nd_scren(fh_1)
                fhn2=''
            else:
                fh_1=self.fihirana_laharana.text()
                fh_2=self.lohateny.text()            
                conf=f" {(fh_2).upper()} "
                fhn=fihirana_G.fihirana2(fh_1,(fh_2).upper())
                #fhn2=fihirana_G.fihirana2_nd_scren(fh_1)
                fhn2=''
                
            return conf,fhn,fhn2,'fhr'
            '''

    def param(self):
        self.Parametre = Parametre_App()
        self.Parametre.show()

    def ecran_2(self):
        try:
            dt_2=self.mod_text()
            self.ecran_2_fctn(dt_2[2],dt_2[0],"./..")
        except:pass
        
    def ecran_2_fctn(self,fl,nat,status):
        #print(fl)
        screens=QApplication.screens()
        #print ("oui")
        #print(fl,nat)
        #self.ecran__2 = MyWidget(fl,nat,status)
        
        
        if self.ecran__2==None:
            self.ecran__2 = MyWidget()
            self.ecran__2.showFullScreen()
            self.second_fenetre_ouverte=True
        else:    
            self.ecran__2.close()
            self.ecran__2=None
            self.second_fenetre_ouverte=False
            
            
        #♣self.ecran__2.show()
        
        # if len(screens)>=2:
        #     second_screen=screens[1]
        #     self.ecran__2 = MyWidget(fl,nat)
        #     self.ecran__2.move(second_screen.geometry().x(), second_screen.geometry().y())
            
        #     self.ecran__2.showFullScreen()
        #     self.ecran__2.show()
        # else:
        #     pass
        #print("   Résolution primaire : {}x{}".format(screen.size().width(), screen.size().height()))    
        # print(len(screens))
        # for screen in screens:
            
        #     if screen.isPrimary():
        #         print("   Résolution primaire : {}x{}".format(screen.size().width(), screen.size().height()))    
        #         pass
        #     else:
        #         print("   Résolution secondaire : {}x{}".format(screen.size().width(), screen.size().height()))
        #         self.ecran__2 = MyWidget(fl,nat)
        #         self.ecran__2.move(second_screen.geometry().x() + 100, second_screen.geometry().y() + 100)
        #         self.ecran__2.show()
                
        # pass
    
    def historique(self):
        # app=QApplication([])
        # screens=QApplication.screens()
        
        # print(len(screens))
        print('oui')
        pass
    
    def vrs(self,inn,xi):
        connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
        curseur_vrs=connexion.cursor()
        curseur_vrs.execute('SELECT * FROM vrs')
        resultats_fihirana2=curseur_vrs.fetchall()
        connexion.close()
        
        for te in resultats_fihirana2:
            if inn==te[2] and xi==te[1]:
                te_=te[3]
                
                break
            else:te_=''
        return te_

    def vrst(self):
        boky=self.comboBox_boky.currentText()
        tko=self.toko.text()
        end=self.vrs(boky,tko)
        if end=='':
            self.andininy.setPlaceholderText(f"--")
        else:    
            self.andininy.setPlaceholderText(f"(1-{self.vrs(boky,tko)})")
            self.label_andininy.setText(f"Andininy (1-{self.vrs(boky,tko)}) :")
        
    def chptr(self):
        boky=self.comboBox_boky.currentText()
        if boky=='':
            self.toko.setPlaceholderText(f" -- ")
        else:
            boky_trad=baiboly_G.trad(boky,1)
            ctn_boky_trad=boky_trad[0]
            tt=ctn_boky_trad[3]
            if tt==1:
                self.toko.setPlaceholderText(f" 1 ")
                self.andininy.setPlaceholderText(f" -- ")
                self.label_toko.setText(f"Toko (1) :")
            else:
                self.toko.setPlaceholderText(f"{tt}")
                self.label_toko.setText(f"Toko (1-{tt}) :")
                self.andininy.setPlaceholderText(f" -- ")
                    #print(tex[1])
            #print(tt)
    
    def initializescdEcran(self):
        self.ecran__2.loadFile("","","")
        
    def affichescndEcran(self,content,nature,status):
        if self.ecran__2!=None:
            self.ecran__2.loadFile(content,nature,status)
        else:pass
        
    def on_tab_clik(self,index):
        if index == 0:
            
            self.label.setText("BAIBOLY")
            self.radioButton_testameta1.setChecked(True)
            self.testmnt1
            self.initializescdEcran()
        elif index == 1:
            self.label.setText("FIHIRANA")
            self.initializescdEcran()
            
        elif index == 2:
            self.label.setText("FIHIRANA FANAMPINY")
            self.initializescdEcran()

    def testmnt1(self):
        self.comboBox_boky.clear()
        new_option = ['Genesisy', 'Eksodosy', 'Levitikosy', 'Nomery', 'Deotoronomia', 'Josoa', 'Mpitsara', 'Rota', 'ISamoela', 'IISamoela', 'IMpanjaka', 'IIMpanjaka', 'ITantara', 'IITantara', 'Ezra', 'Nehemia', 'Estera', 'Joba', 'Salamo', 'Ohabolana', 'Mpitoriteny', 'Tononkira', 'Isaia', 'Jeremia', 'Fitomaniana', 'Ezekiela', 'Daniela', 'Hosea', 'Joela', 'Amosa', 'Obadia', 'Jona', 'Mika', 'Nahoma', 'Habakoka', 'Zefania', 'Hagay', 'Zakaria', 'Malakia']
        self.comboBox_boky.addItems(new_option)
        
    def testmnt2(self):
        self.comboBox_boky.clear()
        new_option = ['Matio', 'Marka', 'Lioka', 'Jaona', 'Asa', 'Romana', 'IKorintiana', 'IIKorintiana', 'Galatiana', 'Efesiana', 'Filipiana', 'Kolosiana', 'ITesaloniana', 'IITesaloniana', 'ITimoty', 'IITimoty', 'Titosy', 'Filemona', 'Hebreo', 'Jakoba', 'IPetera', 'IIPetera', 'IJaona', 'IIJaona', 'IIIJaona', 'Joda', 'Apokalypsy']
        self.comboBox_boky.addItems(new_option)

    def diffusion_btn(self):
        try:
            dt=self.mod_text()
            texte_modifie=dt[1]
            conf=dt[0]
            #output__json=self.output_json()
            #print(texte_modifie)
            
            #list(range(len(text_out)+1),start=1)
            #self.second_interface.mod_text(self.mod_text[0])
            self.label.setText(str(texte_modifie[0]))
            self.conf_view.setText(conf)
            
            self.affichescndEcran(str(texte_modifie[0]),conf,"")
            
            #Save_file(output__json,conf,'BAIBOLY')
        except:
            pass
        
    def ffint(self):
        if self.radioButton_fihirana1.isChecked():
            lh=fihirana_G.fihirana1_get(self.fihirana_laharana.text())
            
            self.lohateny.setText(str(lh[4]).lower())
            self.cles.setText(str(lh[2]))
            fh_1=self.fihirana_laharana.text()
            fh_2=str(lh[4]).lower()           
            self.conf_view_2.setText(f" {(fh_2).upper()} ")
            fhn=fihirana_G.fihirana1(fh_1,(fh_2).upper())
            self.label.setText(str(fhn))
            
        elif self.radioButton_fihirana2.isChecked():
            lh=fihirana_G.fihirana2_get(self.fihirana_laharana.text())
            
            self.lohateny.setText(str(lh[4]).lower())
            self.cles.setText(str(lh[2]))
            fh_1=self.fihirana_laharana.text()
            fh_2=str(lh[4]).lower()           
            self.conf_view_2.setText(f" {(fh_2).upper()} ")
            fhn=fihirana_G.fihirana2(fh_1,(fh_2).upper())
            
            self.label.setText(str(fhn))
            
        else:
            pass
    
    def fihirana_content(self):
        titre=self.label_4.text()
        if titre !="":
            lohateny=fihirana_G.fihiranaf_get(titre)
            self.label.setText(fihirana_G.fihirana_fanampiny(lohateny[1],lohateny[0]))
            self.lineEdit_lohateny.setText(titre)
        else:pass

    def fihirana_f(self):
        titre=self.lineEdit_lohateny.text()
        lohateny=fihirana_G.fihiranaf_get(titre)
        if lohateny!=None:
            self.label_4.setText(str(lohateny[0]))
            
           
        else:
            self.label_4.setText(str(""))
            
        #print((lohateny))
        #
        
               
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    #MainWindow.showFullScreen()
    sys.exit(app.exec_())
