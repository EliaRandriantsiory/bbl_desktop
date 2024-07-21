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
    def __init__(self,donnees,nature):
        super().__init__()
        with open(f"{current_link}\\files//dependances//param.json", "r",encoding='utf-8') as f:
            dt=json.load(f)
        
        ord_diff=len(donnees)
        ffnt=dt['scrn2']
        autr=dt['scrn2_label_size']
        font_sz=ffnt[1]
        font_label_2=ffnt[0]
        size_label_2=[autr[0],autr[1]]
        #baiboly
        nbr_mot_ligne=40

        
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
        txxt=donnees
        #print(txxt)
        self.setStyleSheet(" background-attachment: fixed")
        scroll_area = QScrollArea(self)
        self.label__2 = QLabel()
        self.label__2.setText("")

        # Configuration de la police et du texte
        font = QFont()
        font.setPointSize(font_sz)  
        font.setFamily(font_label_2)  
        self.label__2.setFont(font)
        texte_=self.mod_text(txxt[0],nature)
        if str(nature)=='bbl': 
            self.label__2.setText(texte_)
        elif str(nature)=='fhr':
            self.label__2.setText(txxt[0])
        self.label__2.setAlignment(Qt.AlignCenter)
        self.label__2.setMinimumSize(int(size_label_2[0]),int(size_label_2[1]))
        
        # Configuration de la couleur du texte
        self.label__2.setStyleSheet(f"color: white;background-color: transparent;margin:20")
        self.label__2.setAutoFillBackground(False) 
        #♣self.label__2.setWordWrap()       
        self.label__2.setMargin(100)

        # # Ajout du QLabel dans le ScrollArea
        # scroll_area.setWidget(self.label__2)
        # scroll_area.setStyleSheet("background-color: transparent;border-radius:5")
        # scroll_area.setAlignment(Qt.AlignCenter)
        # """stylesheet"""
        
        # Configuration du fond d'image du ScrollArea
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)

        
        #layout.addWidget(scroll_area)

        # Centrer le contenu verticalement et horizontalement
        

        #self.setLayout(layout)
        self.next_btn=QPushButton(self)
        self.next_btn.setStyleSheet(f"background-color: transparent")
        self.previous_btn=QPushButton(self)
        self.previous_btn.setStyleSheet(f"background-color: transparent")
        self.previous_btn.clicked.connect(lambda:self.previous_file(txxt,nature))
        self.previous_btn.setShortcut('b')
        self.ord_diff_content=QLabel(self)
        self.ord_diff_content.setText(f'Genesisy 2 : 5 ,')
        self.ord_diff_content.setStyleSheet(f"background-color: transparent;padding-top:50")
        
        self.ord_diff_content.setAlignment(QtCore.Qt.AlignCenter)
        self.ord_diff_content.setMinimumSize(QtCore.QSize(50, 0))
        font_title = QtGui.QFont()
        font_title.setFamily("Adobe Garamond Pro")
        font_title.setPointSize(21)
        font_title.setBold(True)
        font_title.setItalic(False)
        #font.setWeight(75)
        self.ord_diff_content.setFont(font_title)
        self.next_btn.clicked.connect(lambda:self.next_file(txxt,nature))
        self.next_btn.setShortcut('n')
            # Création d'un layout vertical pour le Widget principal
        layout = QVBoxLayout(self)
        
        
        layout.addChildWidget(self.ord_diff_content)
        
        layout.addWidget(self.label__2)
        layout.setAlignment(Qt.AlignCenter)
    
    
    def mod_text(self,txx,nature):
        #print(txx)
        with open(f"{current_link}\\files//dependances//param.json", "r",encoding='utf-8') as f:
            dt=json.load(f)
        fnt=dt['scrn2_baiboly']
        if str(nature)=='bbl':
            
            texte_modifie_2=textwrap.wrap(''.join(txx),width=fnt[0])
            texte_modifie_2_='\n'.join(texte_modifie_2)
            #print(texte_modifie_2_)
            #print(nature)
            return texte_modifie_2_
        elif str(nature)=='fhr':
            texte_modifie_2_=''.join(txx)
            return texte_modifie_2_

    def next_file(self,txxt,nature):
        crnt_view=self.ord_diff_content.text()
        crnt_=crnt_view.split(" ")
        if int(crnt_[0])<len(txxt):
            texte_=self.mod_text(txxt[int(crnt_[0])],nature)
            self.label__2.setText(texte_)
        
            crnt_view_=f"{int(crnt_[0])+1} / {len(txxt)}"
            self.ord_diff_content.setText(crnt_view_)
            #print(crnt_view_)
        else:pass
        
    def previous_file(self,txxt,nature):
        crnt_view=self.ord_diff_content.text()
        crnt_=crnt_view.split(" ")
        prev=int(crnt_[0])-2
        #print(crnt_view_)
        if prev>=0:
            #print(prev)
            crnt_view_=f"{int(prev)+1} / {len(txxt)}"
            self.ord_diff_content.setText(crnt_view_)
            texte_=self.mod_text(txxt[prev],nature)
            
            self.label__2.setText(texte_)
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
    print((ff_))
    #print(ff)
    window = MyWidget(ff_,'fhr')
    window.show()
    #window = MyWidget()
    #window2 = MyWidget2()
    #window2.show()
    sys.exit(app.exec_())
