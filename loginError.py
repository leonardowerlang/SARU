# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginInvalido.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginInvalido(object):
    def setupUi(self, loginInvalido):
        loginInvalido.setObjectName("loginInvalido")
        loginInvalido.resize(319, 133)
        loginInvalido.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.label = QtWidgets.QLabel(loginInvalido)
        self.label.setGeometry(QtCore.QRect(80, 20, 161, 31))
        self.label.setMaximumSize(QtCore.QSize(161, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Botao_Sair = QtWidgets.QPushButton(loginInvalido)
        self.Botao_Sair.setGeometry(QtCore.QRect(90, 80, 141, 41))
        self.Botao_Sair.setStyleSheet("")
        self.Botao_Sair.setObjectName("Botao_Sair")
        self.Botao_Sair.clicked.connect(self.btnOk)
        self.label_2 = QtWidgets.QLabel(loginInvalido)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 231, 19))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tela = loginInvalido

        self.retranslateUi(loginInvalido)
        QtCore.QMetaObject.connectSlotsByName(loginInvalido)

    def btnOk(self):
        self.tela.close()

    def retranslateUi(self, loginInvalido):
        _translate = QtCore.QCoreApplication.translate
        loginInvalido.setWindowTitle(_translate("loginInvalido", "Login"))
        self.label.setText(_translate("loginInvalido", "Login Inválido "))
        self.Botao_Sair.setText(_translate("loginInvalido", "OK"))
        self.label_2.setText(_translate("loginInvalido", "Usuário ou senha incorretos"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     loginInvalido = QtWidgets.QDialog()
#     ui = Ui_loginInvalido()
#     ui.setupUi(loginInvalido)
#     loginInvalido.show()
#     sys.exit(app.exec_())

