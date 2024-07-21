from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QFrame
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
def animate_button():
    # Créez une instance de QPropertyAnimation pour l'animation
    print("oui")
    animation = QPropertyAnimation(button, b"geometry")

    # Spécifiez la durée de l'animation (en millisecondes)
    animation.setDuration(1000)

    # Spécifiez les valeurs de départ et d'arrivée de la propriété à animer
    animation.setStartValue(button.geometry())
    animation.setEndValue(button.geometry().translated(400, 300))

    # Démarrez l'animation
    animation.start()

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    window.resize(500,500)

    frame1 = QFrame()
    button = QPushButton("Animate")
    
    button.clicked.connect(animate_button)
    button.setWindowOpacity(0.0)
    animation = QPropertyAnimation(button, b"geometry")
    opacity_animation = QPropertyAnimation(button, b"windowOpacity")

    # Spécifiez la durée de l'animation (en millisecondes)
    animation.setDuration(5000)
    opacity_animation.setDuration(1000)

    # Spécifiez les valeurs de départ et d'arrivée de la propriété à animer
    animation.setStartValue(button.geometry())
    animation.setEndValue(button.geometry().translated(0, 400))
    
    opacity_animation.setStartValue(1.0)
    opacity_animation.setEndValue(0.0)
    
    # Démarrez l'animation
    #animation.start()
    opacity_animation.start()
    

    # Spécifiez la durée de l'animation (en millisecondes)
    

    # Spécifiez les valeurs de départ et d'arrivée de la propriété à animer
    
    
    # Démarrez l'animation
    #animation1.start()
    
    
    

    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(button)
    window.setLayout(layout)

    window.show()
    app.exec()