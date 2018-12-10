# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroJaExiste.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import logo_rc

class Ui_cadastroJaExiste(object):
    def setupUi(self, cadastroJaExiste, msg):
        self.tela = cadastroJaExiste
        cadastroJaExiste.setObjectName("cadastroJaExiste")
        cadastroJaExiste.resize(600, 135)
        icon = QtGui.QIcon.fromTheme("SARU")
        cadastroJaExiste.setWindowIcon(icon)
        cadastroJaExiste.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.Botao_Sair = QtWidgets.QPushButton(cadastroJaExiste)
        self.Botao_Sair.setGeometry(QtCore.QRect(230, 80, 140, 41))
        self.Botao_Sair.setObjectName("Botao_Sair")
        self.Botao_Sair.clicked.connect(self.sair)
        self.labelNome = QtWidgets.QLabel(cadastroJaExiste)
        self.labelNome.setGeometry(QtCore.QRect(30, 30, 540, 31))
        self.labelNome.setMaximumSize(QtCore.QSize(540, 31))
        self.labelNome.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")

        self.retranslateUi(cadastroJaExiste, msg)
        QtCore.QMetaObject.connectSlotsByName(cadastroJaExiste)

    def sair(self):
        self.tela.close()

    def retranslateUi(self, cadastroJaExiste, msg):
        _translate = QtCore.QCoreApplication.translate
        cadastroJaExiste.setWindowTitle(_translate("cadastroJaExiste", "Cadastro"))
        self.Botao_Sair.setText(_translate("cadastroJaExiste", "OK"))
        self.labelNome.setText(_translate("cadastroJaExiste", msg))



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     cadastroJaExiste = QtWidgets.QDialog()
#     ui = Ui_cadastroJaExiste()
#     ui.setupUi(cadastroJaExiste, 'Teste')
#     cadastroJaExiste.show()
#     sys.exit(app.exec_())

