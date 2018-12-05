# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saru.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

class Ui_vendaTickets():
	def setupUi(self, vendaTickets):
		# Background
		vendaTickets.setObjectName("vendaTickets")
		vendaTickets.resize(800, 600)
		vendaTickets.setStyleSheet("background-color: rgb(247, 247, 247);")
		# Linha que separa o 'menu' da compra
		self.graphicsViewFoto = QtWidgets.QGraphicsView(vendaTickets)
		self.graphicsViewFoto.setGeometry(QtCore.QRect(340, 0, 1, 1080))
		self.graphicsViewFoto.setObjectName("graphicsViewFoto")
		# Menu
		# Botão do menu de 'Comprar fichas'
		self.menuComprarButton = QtWidgets.QPushButton(vendaTickets)
		self.menuComprarButton.setGeometry(QtCore.QRect(340, 0, 240, 41))
		self.menuComprarButton.setObjectName("menuComprarButton")
		# Botão do menu de 'Solicitar Cartão'
		self.menuSolicitarButton = QtWidgets.QPushButton(vendaTickets)
		self.menuSolicitarButton.setGeometry(QtCore.QRect(570, 0, 230, 41))
		self.menuSolicitarButton.setObjectName("menuSolicitarButton")
		# Imagem do usuário
		self.imgUsuario = QtWidgets.QLabel(vendaTickets)
		self.pixmap = QPixmap('logo_grande.png')
		self.pixmap = self.pixmap.scaled(300, 300);
		self.imgUsuario.setPixmap(self.pixmap)
		self.imgUsuario.setGeometry(QtCore.QRect(20, 20, 300, 300))
		# Mesagem de Bem Vindo
		self.msgBemVindo = QtWidgets.QLabel(vendaTickets)
		self.msgBemVindo.setGeometry(QtCore.QRect(20, 350, 300, 20))
		self.msgBemVindo.setObjectName("msgBemVindo")
		# Quatidade de fichas atual
		self.msgQtdFichas = QtWidgets.QLabel(vendaTickets)
		self.msgQtdFichas.setGeometry(QtCore.QRect(20, 410, 300, 20))
		self.msgQtdFichas.setObjectName("msgQtdFichas")
		# Número de fichas atuais
		self.numFichas = QtWidgets.QLabel(vendaTickets)
		self.numFichas.setGeometry(QtCore.QRect(20, 430, 300, 20))
		self.numFichas.setObjectName("numFichas")
		# Quatidade de acesso ao RU
		self.msgQtdAcessoRU = QtWidgets.QLabel(vendaTickets)
		self.msgQtdAcessoRU.setGeometry(QtCore.QRect(20, 490, 300, 20))
		self.msgQtdAcessoRU.setObjectName("msgQtdAcessoRU")
		# Número de acesso ao RU
		self.numAcesso = QtWidgets.QLabel(vendaTickets)
		self.numAcesso.setGeometry(QtCore.QRect(20, 510, 300, 20))
		self.numAcesso.setObjectName("numAcesso")
		# Label da novas fichas
		self.msgNovasFichas = QtWidgets.QLabel(vendaTickets)
		self.msgNovasFichas.setGeometry(QtCore.QRect(405, 240, 329, 20))
		self.msgNovasFichas.setObjectName("msgNovasFichas")
		# Input da novas fichas
		self.inputFichas = QtWidgets.QLineEdit(vendaTickets)
		self.inputFichas.setGeometry(QtCore.QRect(405, 280, 329, 30))
		self.inputFichas.setObjectName("inputFichas")
		#Botão de compra
		self.comprarButton = QtWidgets.QPushButton(vendaTickets)
		self.comprarButton.setGeometry(QtCore.QRect(405, 330, 329, 41))
		self.comprarButton.setObjectName("comprarButton")

		self.retranslateUi(vendaTickets)
		QtCore.QMetaObject.connectSlotsByName(vendaTickets)

	def retranslateUi(self, sarulogin):
		_translate = QtCore.QCoreApplication.translate
		vendaTickets.setWindowTitle(_translate("vendaTickets", "Solicitar Cartão"))
		# Mensagem de Bem Vindo
		self.msgBemVindo.setText(_translate("vendaTickets", "Bem Vindo, Fulano!"))
		# Quatidade de fichas atual
		self.msgQtdFichas.setText(_translate("vendaTickets", "Quantidade atual de fichas:"))
		# Número de fichas atuais
		self.numFichas.setText(_translate("vendaTickets", "20"))
		# Quatidade de acesso ao RU
		self.msgQtdAcessoRU.setText(_translate("vendaTickets", "Acessos ao Restaurante Universitário:"))
		# Número de fichas atuais
		self.numAcesso.setText(_translate("vendaTickets", "380"))
		# Label da novas fichas
		self.msgNovasFichas.setText(_translate("vendaTickets", "Insira a quantidade de fichas que deseja comprar"))
		# Botão de compra
		self.comprarButton.setText(_translate("vendaTickets", "Comprar"))
		# Botão do menu de 'Comprar fichas'
		self.menuComprarButton.setText(_translate("vendaTickets", "Comprar fichas"))
		# Botão do menu de 'Solicitar Cartão'
		self.menuSolicitarButton.setText(_translate("vendaTickets", "Solicitar Cartão"))


import logo_rc

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	vendaTickets = QtWidgets.QMainWindow()
	ui = Ui_vendaTickets()
	ui.setupUi(vendaTickets)
	vendaTickets.show()
	sys.exit(app.exec_())