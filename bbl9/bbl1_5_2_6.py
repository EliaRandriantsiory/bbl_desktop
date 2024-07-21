import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QLabel, QVBoxLayout,QPushButton
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
import os,json,textwrap,sqlite3
from PIL import Image,ImageEnhance
import add_fonction_snd

current_link=os.getcwd()
image_path__=f"{current_link}//files//images//image_sombre.jpg"
chm_baiboly=f"{current_link}//files//DB//baiboly"
chm_fihirana=f"{current_link}//files//DB//fihirana"
chm_json_scrn1=f"{current_link}//files//dependances//scrn1_out.json"


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        #print("oui")
        with open(f"{current_link}\\files//dependances//param.json", "r",encoding='utf-8') as f:
            dt=json.load(f)
        
        # ord_diff=len(donnees)
        # ffnt=dt['scrn2']
        # autr=dt['scrn2_label_size']
        # font_sz=ffnt[1]
        # font_label_2=ffnt[0]
        # size_label_2=[autr[0],autr[1]]
        
        # #baiboly
        # nbr_mot_ligne=40

        
        #im=Image.open(image_path__)
        #brt=ImageEnhance.Brightness(im)
        #brightness_level=1
        #image_path_=brt.enhance(brightness_level)
        #image_path_.save(f"{current_link}//image_sombre.jpg")
        #im.close()


        # Création d'une image QPixmap à partir de votre image
        image_path =image_path__
        image = QImage(image_path)
        pixmap = QPixmap.fromImage(image)
        #txxt=donnees
        #print(txxt)
        self.setObjectName("self")
        self.setStyleSheet(f"back")
        #self.resize(1522, 710)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.contextContent = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.contextContent.setFont(font)
        self.contextContent.setStyleSheet(f"margin-right:10")
        self.contextContent.setObjectName("contextContent")
        self.gridLayout.addWidget(self.contextContent, 0, 0, 1, 1)
        self.content = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("MS Mincho")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.content.setFont(font)
        #self.content.setStyleSheet(f"margin-right:50")
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setLineWidth(0)
        self.content.setTextFormat(QtCore.Qt.AutoText)
        self.content.setScaledContents(True)
        self.content.setAlignment(QtCore.Qt.AlignCenter)
        self.content.setWordWrap(True)
        self.content.setObjectName("content")
        self.gridLayout.addWidget(self.content, 1, 0, 1, 2)
        self.nbrWrap = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.nbrWrap.setFont(font)
        self.nbrWrap.setStyleSheet(f"margin-Left:-10")
        self.nbrWrap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nbrWrap.setObjectName("nbrWrap")
        self.gridLayout.addWidget(self.nbrWrap, 2, 1, 1, 1)
        self.content.setMargin(80)
        
        
        #self.loadFile(donnees,nature,status)
        
        
        # 
        
        
    def mod_text(self,txx,nature):
        #print(txx)
        with open(f"{current_link}\\files//dependances//param.json", "r",encoding='utf-8') as f:
            dt=json.load(f)
        fnt=dt['scrn2_baiboly']
        if str(nature)=='bbl':
            
            texte_modifie_2=textwrap.wrap(''.join(txx),width=fnt[0])
            texte_modifie_2_=''.join(texte_modifie_2)
            #print(texte_modifie_2_)
            #print(nature)
            return texte_modifie_2_
        elif str(nature)=='fhr':
            texte_modifie_2_=''.join(txx)
            return texte_modifie_2_
    
    def load(self,str):
        self.content.setText(str)
        print("oui")
        #self.loadFile(self.donnes,self.nature,self.status)
    
    
    def loadFile(self,fl,nature,status):
        #texte_modifie_2_=''.join(fl)
        self.contextContent.setText(nature)
        self.content.setText(fl)
        self.nbrWrap.setText(status)

    def next_file(self,txxt,nature):
        crnt_view=self.nbrWrap.text()
        crnt_=crnt_view.split(" ")
        if int(crnt_[0])<len(txxt):
            texte_=self.mod_text(txxt[int(crnt_[0])],nature)
            self.content.setText(texte_)
        
            crnt_view_=f"{int(crnt_[0])+1} / {len(txxt)}"
            self.nbrWrap.setText(crnt_view_)
            #print(crnt_view_)
        else:pass
        
    def previous_file(self,txxt,nature):
        crnt_view=self.nbrWrap.text()
        crnt_=crnt_view.split(" ")
        prev=int(crnt_[0])-2
        #print(crnt_view_)
        if prev>=0:
            #print(prev)
            crnt_view_=f"{int(prev)+1} / {len(txxt)}"
            self.nbrWrap.setText(crnt_view_)
            texte_=self.mod_text(txxt[prev],nature)
            
            self.content.setText(texte_)
        else:pass

 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ff_=["Tsy misy tantara Izay mamin’ny foko \n Toy ny tantaran’i Jeso! \nTantara mambabo ny foko tokoa \nTantarao amiko indray\n",
        "Isan'andininy:\nTantarao indray (bis)\n(Mba tantarao) Iny Jesosy tsy foiko, \nTantarao indray\n",
        "2.\nTsy misy tantara Izay mamin’ ny foko \nToy ny tantaran’ i Jeso! \nTantara tsy lefy, Tsy maintsy ho to, \nTantarao amiko indray\n",
        "3.\nTsy misy tantara ilaiko ety \nToy ny tantaran’i Jeso!\nTantara ilaiko hanampy ahy ety \nTantarao amiko indray"]
    ffb_=["5 Ny hazo madinika famboly dia tsy mbola nisy teo amin'ny tany, ary ny anana famboly tsy mbola nisy naniry; fa tsy mbola nampilatsaka ranonorana tambonin'ny tany Jehovah Andriamanitra, ary nisy olona hiasa ny tany; 6", "nefa nisy zavona niakatra avy tamin'ny tany ka nandena ny tany rehetra. 7 Ary vovo-tany no namoronan'i Jehovah Andriamanitra ny olona, ary nofofoniny fofonaina mahavelona ny vavorony; dia tonga olombelona izy. 8 Ary", 'Jehovah Andriamanitra nanao saha tao Edena tany atsinanana, ka napetrany tao ralehilahy izay noforoniny.']
    ff=''.join(ff_)
    # connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
    # curseur = connexion.cursor()
    # curseur.execute("SELECT content FROM scrn1_out")
    # result=curseur.fetchone()
    # result=result[0]
    # #result=list(result)
    # ff=''.join(result)
    #print((ff))
    #print(ff)
    #window = MyWidget(ff,'fhr')
    window = MyWidget()
    window.show()
    #window = MyWidget()
    #window2 = MyWidget2()
    #window2.show()
    sys.exit(app.exec_())
