from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *



from login import Ui_Dialog
from registrar import Ui_MainWindow
from perfilconta import Ui_logado


class Perfil(QMainWindow):
    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_logado()
        self.ui.setupUi(self)
        self.ui.actionConta.triggered.connect(self.perfil)

    def perfil(self):
        pass

class TelaLogin(QDialog):

    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Botoes
        self.ui.pushButton.clicked.connect(self.botao_login)
        self.ui.pushButton_2.clicked.connect(self.botao_ir_para_registrar)

    def botao_login(self):
        return self.usuario_and_senha()

    def botao_ir_para_registrar(self):
        self.tela_register = Registrar()
        self.tela_register.show()
        self.close()

    def usuario_and_senha(self):
        usuario = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()

        with open("arquivo.txt", "r") as arquivo:
            ler = arquivo.read()
            if usuario == "" and senha == "":
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Digite algo")

                iniciar = msg.exec_()
            elif usuario in ler and senha in ler:
                self.tela_voltar_login = Perfil()
                self.tela_voltar_login.show()
                self.close()

            elif usuario != ler and senha != ler:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Digite A senha Correta")

                iniciar = msg.exec_()

class Registrar(QMainWindow):
    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.botao_terminar_cadastro)

    def botao_terminar_cadastro(self):
        return self.usuario_senha()

    def usuario_senha(self):
        gmail = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()
        senha_confirm = self.ui.lineEdit_3.text()

        if senha == "" and senha_confirm == "" and gmail == "":
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Digite algo")

            iniciar = msg.exec_()
        elif senha == senha_confirm:
            msg = QMessageBox()
            msg.setWindowTitle("Registrado")
            msg.setText("Registrado")

            iniciar = msg.exec_()
            with open("arquivo.txt", "a") as arquivo:
                arquivo.write((gmail) + "\n" + (senha) +  "\n" + (senha_confirm) + "\n")
                self.voltar = TelaLogin()
                self.voltar.show()
                self.close()
        elif senha != senha_confirm:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Senhas Diferentes")

            iniciar = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Tente Novamente mais tarde")

            iniciar = msg.exec_()


if __name__ == "__main__":
    import os,sys
    app = QApplication(sys.argv)
    window = TelaLogin()
    window.show()
    sys.exit(app.exec_())