import csv
import pathlib
import sys
import textwrap

from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QStatusBar,
    QToolBar,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit, 
)


class MainPanel(QWidget):
    """Panel principal."""

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window


        layoutV = QVBoxLayout()
        self.setLayout(layoutV)


        self.label = QLabel("Directorio:",)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutV.addWidget(self.label)


        layoutH1 = QHBoxLayout()
        layoutV.addLayout(layoutH1)

        layoutH2 = QHBoxLayout()
        layoutV.addLayout(layoutH2)


        self.label2 = QLabel("Tamaño Limite:")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutH1.addWidget(self.label2)
        
        self.label3 = QLineEdit(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutH1.addWidget(self.label3)

        self.label4 = QLabel("4" )
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutH2.addWidget(self.label4)

        self.label5  = QLabel("5" )
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutH2.addWidget(self.label5)
        

        #button = QPushButton("Abrir Directorio")
        #button.clicked.connect(self.main_window.on_open)
        #layout.addWidget(button)

class Window(QMainWindow):
    """Ventana principal."""

    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.setWindowTitle("Aplicacion Para Mami")
        self.setWindowIcon(QIcon("icon.png"))
  

        # menú y barra de herramientas
        toolbar = QToolBar("main-toolbar")
        self.addToolBar(toolbar)
        self._status_bar = QStatusBar(self)
        self.setStatusBar(self._status_bar)
        menubar = self.menuBar()

        

        # las diferentes acciones tanto para el menu como para la barra de herramientas
        open_action = QAction(QIcon.fromTheme("document-open"), "Abrir archivo", self)
        open_action.setToolTip("Abrir archivo de datos")
        open_action.triggered.connect(self.on_open)
        open_action.setShortcut('Ctrl+A')
        quit_action = QAction(QIcon(), "Salir", self)
        quit_action.triggered.connect(app.exit)
        about_action = QAction(QIcon(), "Acerca de...", self)
        about_action.triggered.connect(self.on_about)

        # configuramos la barra de herramientas
        #toolbar.addAction(open_action)

        # configuramos el menú
        menu = menubar.addMenu("&Archivo")
        menu.addAction(open_action)
        menu.addAction(quit_action)
        menu = menubar.addMenu("A&yuda")
        menu.addAction(about_action)

        self.main_panel = MainPanel(self)
        self.setCentralWidget(self.main_panel)

        self.set_status("Comenzando")


    def set_status(self, message):
        """Muestra un mensaje efímero en la barra de estado."""
        self._status_bar.showMessage(message, 3000)

    def show_error(self, message):
        """Muestra un mensaje de error via un diálogo y en la barra de estado."""
        self.set_status(f"Error: {message}")
        QMessageBox.critical(self, "Error", message)

    def on_open(self):
        """Abre un nuevo archivo de datos y refresca el widget principal."""
        self.set_status("Abriendo archivo con datos")

        # abrimos un diálogo para que se seleccione un archivo
        dirpath = QFileDialog.getExistingDirectory(self, "Abrir archivo")
        print("============dirpath",repr(dirpath))
        if not dirpath:
            self.set_status("Ningún archivo seleccionado")
            return
        
        self.main_panel.label.setText("Directorio:" + dirpath)

        


    def on_about(self):
        """Muestra el diálogo de Acerca de."""
        title = "AplicacionParaMami"
        text = textwrap.dedent("""
            Ejemplo de aplicación gráfica para el libro
            Python en Ámbitos Científicos
            de Facundo Batista y Manuel Carlevaro

            http://pyciencia.taniquetil.com.ar/
        """)
        QMessageBox.about(self, title, text)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
