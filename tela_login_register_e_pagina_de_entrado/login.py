# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telalogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 575)
        Dialog.setStyleSheet("")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 190, 451, 51))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    font-size: 16px;\n"
"    font-family:Arial,Helvetica,sans-serif;\n"
"    \n"
"    padding-left: 10px;    \n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 260, 451, 51))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    font-size: 16px;\n"
"    font-family:Arial,Helvetica,sans-serif;\n"
"    \n"
"    padding-left: 10px;    \n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 450, 211, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 340, 211, 61))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: black;\n"
"    font-size: 20px;\n"
"    \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Usuario"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Senha"))
        self.pushButton.setText(_translate("Dialog", "Log in"))
        self.pushButton_2.setText(_translate("Dialog", "Registrar"))
