from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

if __name__ == '__main__':
    app = QApplication([])

    # Création de la fenêtre principale
    window = QMainWindow()

    # Création d'une instance de QWebEngineView
    webview = QWebEngineView()

    # Chargement d'une page HTML locale
    webview.setHtml('''
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="bootstrap.min.css">
        </head>
        <body>
            <h1>Exemple d'utilisation de Bootstrap dans PyQt5</h1>
            <button class="btn btn-primary">Bouton Bootstrap</button>
            
            <!-- Inclure ici les scripts JavaScript de Bootstrap, le cas échéant -->
        </body>
        </html>
    ''')

    # Ajout du QWebEngineView à la fenêtre principale
    window.setCentralWidget(webview)

    # Affichage de la fenêtre
    window.show()

    app.exec()