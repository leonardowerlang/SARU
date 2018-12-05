# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroJaExiste.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cadastroJaExiste(object):
    def setupUi(self, cadastroJaExiste):
        cadastroJaExiste.setObjectName("cadastroJaExiste")
        cadastroJaExiste.resize(320, 135)
        icon = QtGui.QIcon.fromTheme("SARU")
        cadastroJaExiste.setWindowIcon(icon)
        cadastroJaExiste.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.Botao_Sair = QtWidgets.QPushButton(cadastroJaExiste)
        self.Botao_Sair.setGeometry(QtCore.QRect(80, 80, 141, 41))
        self.Botao_Sair.setObjectName("Botao_Sair")
        self.labelNome = QtWidgets.QLabel(cadastroJaExiste)
        self.labelNome.setGeometry(QtCore.QRect(30, 30, 281, 31))
        self.labelNome.setMaximumSize(QtCore.QSize(281, 31))
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

        self.retranslateUi(cadastroJaExiste)
        QtCore.QMetaObject.connectSlotsByName(cadastroJaExiste)

    def retranslateUi(self, cadastroJaExiste):
        _translate = QtCore.QCoreApplication.translate
        cadastroJaExiste.setWindowTitle(_translate("cadastroJaExiste", "Cadastro"))
        self.Botao_Sair.setText(_translate("cadastroJaExiste", "Sair"))
        self.labelNome.setText(_translate("cadastroJaExiste", "Matrícula já cadastrada!"))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastroJaExiste = QtWidgets.QDialog()
    ui = Ui_cadastroJaExiste()
    ui.setupUi(cadastroJaExiste)
    cadastroJaExiste.show()
    sys.exit(app.exec_())

