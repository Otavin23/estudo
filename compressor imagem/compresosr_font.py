from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from compress import Ui_MainWindow

class Tela(QMainWindow):
    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.botao_novo)

    def botao_novo(self):

        ler = QtWidgets.QFileDialog.getOpenFileName()[0]
        with open(ler, "r") as a:
            leitura = a.read()
            print(leitura)


if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = Tela()
    window.show()
    sys.exit(app.exec_())
