# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import solicitacoes
import cadastro
import login

class Ui_Home(object):
    def setupUi(self, Home):
        self.tela = Home
        Home.setObjectName("Home")
        Home.resize(242, 300)
        Home.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.logo = QtWidgets.QLabel(Home)
        self.logo.setGeometry(QtCore.QRect(100, 20, 51, 51))
        self.logo.setObjectName("logo")
        self.Botao_Solicitacao = QtWidgets.QPushButton(Home)
        self.Botao_Solicitacao.setGeometry(QtCore.QRect(10, 110, 221, 25))
        self.Botao_Solicitacao.setObjectName("Botao_Solicitacao")
        self.Botao_Solicitacao.clicked.connect(self.verSolicitacoes)

        self.Botao_Cadastro = QtWidgets.QPushButton(Home)
        self.Botao_Cadastro.setGeometry(QtCore.QRect(10, 140, 221, 25))
        self.Botao_Cadastro.setObjectName("Botao_Cadastro")
        self.Botao_Cadastro.clicked.connect(self.cadastrar)


        self.Botao_Sair = QtWidgets.QPushButton(Home)
        self.Botao_Sair.setGeometry(QtCore.QRect(70, 260, 101, 25))
        self.Botao_Sair.setObjectName("Botao_Sair")
        self.Botao_Sair.clicked.connect(self.sair)

        self.msg_wlcm = QtWidgets.QLabel(Home)
        self.msg_wlcm.setGeometry(QtCore.QRect(20, 80, 201, 20))
        self.msg_wlcm.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_wlcm.setObjectName("msg_wlcm")

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def verSolicitacoes(self):
        self.tela.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = solicitacoes.Ui_Solicitacao()
        self.ui.setupUi(self.window)
        self.window.show()

    def cadastrar(self):
        self.tela.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = cadastro.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def sair(self):
        self.tela.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = login.Ui_sarulogin()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home"))
        self.logo.setText(_translate("Home", "<html><head/><body><p><img src=\"logo.png\"/></p></body></html>"))
        self.Botao_Solicitacao.setText(_translate("Home", "Verificar solicitações de cartões"))
        self.Botao_Cadastro.setText(_translate("Home", "Cadastrar Estudante"))
        self.Botao_Sair.setText(_translate("Home", "Sair"))
        self.msg_wlcm.setText(_translate("Home", "Bem vindo!"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Home = QtWidgets.QDialog()
#     ui = Ui_Home()
#     ui.setupUi(Home)
#     Home.show()
#     sys.exit(app.exec_())
