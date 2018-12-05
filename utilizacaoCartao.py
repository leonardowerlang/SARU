# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saru.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

class Ui_utilizacaoCartao():
	def setupUi(self, utilizacaoCartao):
		# Background
		utilizacaoCartao.setObjectName("utilizacaoCartao")
		utilizacaoCartao.resize(800, 600)
		utilizacaoCartao.setStyleSheet("background-color: rgb(247, 247, 247);")
		# Imagem do usuário
		self.imgUsuario = QtWidgets.QLabel(utilizacaoCartao)
		self.pixmap = QPixmap('logo_grande.png')
		self.pixmap = self.pixmap.scaled(300, 300);
		self.imgUsuario.setPixmap(self.pixmap)
		self.imgUsuario.setGeometry(QtCore.QRect(250, 20, 300, 300))
		# Mesagem de Bem Vindo
		self.msgBemVindo = QtWidgets.QLabel(utilizacaoCartao)
		self.msgBemVindo.setGeometry(QtCore.QRect(250, 350, 300, 20))
		self.msgBemVindo.setObjectName("msgBemVindo")
		# Quatidade de fichas atual
		self.msgQtdFichas = QtWidgets.QLabel(utilizacaoCartao)
		self.msgQtdFichas.setGeometry(QtCore.QRect(250, 410, 300, 20))
		self.msgQtdFichas.setObjectName("msgQtdFichas")
		# Número de fichas atuais
		self.numFichas = QtWidgets.QLabel(utilizacaoCartao)
		self.numFichas.setGeometry(QtCore.QRect(250, 430, 300, 20))
		self.numFichas.setObjectName("numFichas")
		# Quatidade de acesso ao RU
		self.msgQtdAcessoRU = QtWidgets.QLabel(utilizacaoCartao)
		self.msgQtdAcessoRU.setGeometry(QtCore.QRect(250, 490, 300, 20))
		self.msgQtdAcessoRU.setObjectName("msgQtdAcessoRU")
		# Número de acesso ao RU
		self.numAcesso = QtWidgets.QLabel(utilizacaoCartao)
		self.numAcesso.setGeometry(QtCore.QRect(250, 510, 300, 20))
		self.numAcesso.setObjectName("numAcesso")

		self.retranslateUi(utilizacaoCartao)
		QtCore.QMetaObject.connectSlotsByName(utilizacaoCartao)

	def retranslateUi(self, sarulogin):
		_translate = QtCore.QCoreApplication.translate
		utilizacaoCartao.setWindowTitle(_translate("utilizacaoCartao", "Utilização de Cartões"))
		# Mensagem de Bem Vindo
		self.msgBemVindo.setText(_translate("utilizacaoCartao", "Bem Vindo, Fulano!"))
		# Quatidade de fichas atual
		self.msgQtdFichas.setText(_translate("utilizacaoCartao", "Quantidade atual de fichas:"))
		# Número de fichas atuais
		self.numFichas.setText(_translate("utilizacaoCartao", "20"))
		# Quatidade de acesso ao RU
		self.msgQtdAcessoRU.setText(_translate("utilizacaoCartao", "Acessos ao Restaurante Universitário:"))
		# Número de fichas atuais
		self.numAcesso.setText(_translate("utilizacaoCartao", "380"))


import logo_rc

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	utilizacaoCartao = QtWidgets.QMainWindow()
	ui = Ui_utilizacaoCartao()
	ui.setupUi(utilizacaoCartao)
	utilizacaoCartao.show()
	sys.exit(app.exec_())