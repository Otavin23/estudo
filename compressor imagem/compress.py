# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compressoor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 430)
        MainWindow.setStyleSheet("background-color: white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 310, 231, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 255, 0);\n"
"    font-size: 19px; \n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 321, 71))
        self.label.setStyleSheet("QLabel{\n"
"    font-size: 29px;\n"
"}")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 70, 371, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color:  rgb(0, 170, 255);\n"
"    font-size: 19px; \n"
"    color: white;\n"
"    \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 130, 171, 41))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    padding-left: 10px;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    \n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 130, 181, 41))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    padding-left: 10px;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    \n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 210, 371, 16))
        self.label_2.setStyleSheet("font-size: 17px;\n"
"")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Converter"))
        self.label.setText(_translate("MainWindow", "Compressor de imagem"))
        self.pushButton_2.setText(_translate("MainWindow", "+Novo"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Digite nova altura"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Digite nova Largura"))
        self.label_2.setText(_translate("MainWindow", "---------------------------------------------------------------------------------------------------"))
