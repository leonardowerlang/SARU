# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import solicitarCartao
import loginError
import cadastro
import hashlib
import logo_rc
import admin
import banco
import sys

class Ui_sarulogin(object):
    def setupUi(self, sarulogin):
        sarulogin.setObjectName("sarulogin")
        sarulogin.resize(651, 398)
        sarulogin.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.centralwidget = QtWidgets.QWidget(sarulogin)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 230, 231, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 270, 231, 27))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 40, 131, 141))
        self.label_3.setObjectName("label_3")
        self.Botao_Login = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Login.setGeometry(QtCore.QRect(210, 310, 231, 27))
        self.Botao_Login.setStyleSheet("background-color: rgb(63, 114, 105);")
        self.Botao_Login.setObjectName("Botao_Login")
        self.Botao_Login.clicked.connect(self.btnLogar)

        self.Botao_LoginAdm = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_LoginAdm.setGeometry(QtCore.QRect(210, 340, 231, 27))
        self.Botao_LoginAdm.setStyleSheet("background-color: rgb(63, 114, 105);")
        self.Botao_LoginAdm.setObjectName("Botao_LoginAdm")
        self.Botao_LoginAdm.clicked.connect(self.btnLogarAdm)

        sarulogin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(sarulogin)
        self.statusbar.setObjectName("statusbar")
        sarulogin.setStatusBar(self.statusbar)

        self.retranslateUi(sarulogin)
        QtCore.QMetaObject.connectSlotsByName(sarulogin)
        self.tela = sarulogin

    def btnLogar(self):
        h = hashlib.sha1()
        h.update((self.lineEdit_2.text()).encode('utf-8'))
        temp = banco.Banco().logar(self.lineEdit.text(), h.hexdigest())
        if temp:
            solic = banco.Banco().solicitou(temp[0])

            self.tela.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = solicitarCartao.Ui_solicitarCartao(temp, solic)
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = loginError.Ui_loginInvalido()
            self.ui.setupUi(self.window)
            self.window.show()

    def btnLogarAdm(self):
        h = hashlib.sha1()
        h.update((self.lineEdit_2.text()).encode('utf-8'))
        temp = banco.Banco().logarAdm(self.lineEdit.text(), h.hexdigest())
        if temp:
            self.tela.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = admin.Ui_Home()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = loginError.Ui_loginInvalido()
            self.ui.setupUi(self.window)
            self.window.show()

    def retranslateUi(self, sarulogin):
        _translate = QtCore.QCoreApplication.translate
        sarulogin.setWindowTitle(_translate("sarulogin", "Saru Login"))
        self.lineEdit.setToolTip(_translate("sarulogin", "Digite seu login"))
        self.lineEdit.setPlaceholderText(_translate("sarulogin", "Login", "Login"))
        self.lineEdit_2.setPlaceholderText(_translate("sarulogin", "Senha"))
        self.label_3.setText(_translate("sarulogin", "<html><head/><body><p><img src=\"logo_grande.png\"/></p></body></html>"))
        self.Botao_Login.setText(_translate("sarulogin", "Logar"))
        self.Botao_LoginAdm.setText(_translate("sarulogin", "Logar como Administrador"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     sarulogin = QtWidgets.QMainWindow()
#     ui = Ui_sarulogin()
#     ui.setupUi(sarulogin)
#     sarulogin.show()
#     sys.exit(app.exec_())