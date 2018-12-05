# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saru.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import logo_rc
import banco
import login

class Cliente:
	def __init__(self, id, nome, fichas, acessos, solcitou):
		self.id = id
		self.nome = nome
		self.qtdFichas = fichas
		self.acessoRU = acessos
		self.solcitou = solcitou

class Ui_solicitarCartao(object):
	def __init__(self, cliente, solcitou):
		self.cliente = Cliente(cliente[0], cliente[1], cliente[2], cliente[3], solcitou)

	def setupUi(self, solicitarCartao):
		self.tela = solicitarCartao
		# Background
		solicitarCartao.setObjectName("solicitarCartao")
		solicitarCartao.resize(800, 600)
		solicitarCartao.setStyleSheet("background-color: rgb(247, 247, 247);")
		# Linha que separa o 'menu' da compra
		self.graphicsViewFoto = QtWidgets.QGraphicsView(solicitarCartao)
		self.graphicsViewFoto.setGeometry(QtCore.QRect(340, 0, 1, 1080))
		self.graphicsViewFoto.setObjectName("graphicsViewFoto")
		# Menu
		# Botão do menu de 'Comprar fichas'
		self.menuComprarButton = QtWidgets.QPushButton(solicitarCartao)
		self.menuComprarButton.setGeometry(QtCore.QRect(340, 0, 230, 41))
		self.menuComprarButton.setObjectName("menuComprarButton")
		self.menuComprarButton.clicked.connect(self.telaComprarFichas)
		# Botão do menu de 'Solicitar Cartão'
		self.menuSolicitarButton = QtWidgets.QPushButton(solicitarCartao)
		self.menuSolicitarButton.setGeometry(QtCore.QRect(570, 0, 230, 41))
		self.menuSolicitarButton.setObjectName("menuSolicitarButton")
		self.menuSolicitarButton.clicked.connect(self.telaSolicitarCartao)
		# Imagem do usuário
		self.imgUsuario = QtWidgets.QLabel(solicitarCartao)
		self.pixmap = QPixmap('logo_grande.png')
		self.pixmap = self.pixmap.scaled(300, 300);
		self.imgUsuario.setPixmap(self.pixmap)
		self.imgUsuario.setGeometry(QtCore.QRect(20, 20, 300, 300))
		# Mesagem de Bem Vindo
		self.msgBemVindo = QtWidgets.QLabel(solicitarCartao)
		self.msgBemVindo.setGeometry(QtCore.QRect(20, 350, 300, 20))
		self.msgBemVindo.setObjectName("msgBemVindo")
		# Quatidade de fichas atual
		self.msgQtdFichas = QtWidgets.QLabel(solicitarCartao)
		self.msgQtdFichas.setGeometry(QtCore.QRect(20, 410, 300, 20))
		self.msgQtdFichas.setObjectName("msgQtdFichas")
		# Número de fichas atuais
		self.numFichas = QtWidgets.QLabel(solicitarCartao)
		self.numFichas.setGeometry(QtCore.QRect(20, 430, 300, 20))
		self.numFichas.setObjectName("numFichas")
		# Quatidade de acesso ao RU
		self.msgQtdAcessoRU = QtWidgets.QLabel(solicitarCartao)
		self.msgQtdAcessoRU.setGeometry(QtCore.QRect(20, 490, 300, 20))
		self.msgQtdAcessoRU.setObjectName("msgQtdAcessoRU")
		# Número de acesso ao RU
		self.numAcesso = QtWidgets.QLabel(solicitarCartao)
		self.numAcesso.setGeometry(QtCore.QRect(20, 510, 300, 20))
		self.numAcesso.setObjectName("numAcesso")
		# Label de solicitação
		self.msgNovoCart = QtWidgets.QLabel(solicitarCartao)
		self.msgNovoCart.setGeometry(QtCore.QRect(430, 240, 358, 20))
		self.msgNovoCart.setObjectName("msgNovoCart")
		self.msgNovoCart.hide()
		#MSG de cartao ja solicitado
		self.msgSolCart = QtWidgets.QLabel(solicitarCartao)
		self.msgSolCart.setGeometry(QtCore.QRect(430, 240, 358, 20))
		self.msgSolCart.setObjectName("msgSolCart")
		self.msgSolCart.hide()
		#Botão de solicitação
		self.solicitarCartao = QtWidgets.QPushButton(solicitarCartao)
		self.solicitarCartao.setGeometry(QtCore.QRect(405, 280, 329, 41))
		self.solicitarCartao.setObjectName("solicitarCartao")
		self.solicitarCartao.clicked.connect(self.solicCartao)
		self.solicitarCartao.hide()
		# Label da novas fichas
		self.msgNovasFichas = QtWidgets.QLabel(solicitarCartao)
		self.msgNovasFichas.setGeometry(QtCore.QRect(445, 240, 329, 20))
		self.msgNovasFichas.setObjectName("msgNovasFichas")
		# Input da novas fichas
		self.inputFichas = QtWidgets.QLineEdit(solicitarCartao)
		self.inputFichas.setGeometry(QtCore.QRect(405, 280, 329, 30))
		self.inputFichas.setObjectName("inputFichas")
		#Botão de compra
		self.comprarButton = QtWidgets.QPushButton(solicitarCartao)
		self.comprarButton.setGeometry(QtCore.QRect(405, 330, 329, 41))
		self.comprarButton.setObjectName("comprarButton")
		self.comprarButton.clicked.connect(self.comprarFichas)
		#Botão de sair
		self.sair = QtWidgets.QPushButton(solicitarCartao)
		self.sair.setGeometry(QtCore.QRect(20, 550, 300, 41))
		self.sair.setObjectName("sair")
		self.sair.clicked.connect(self.logout)

		self.retranslateUi(solicitarCartao)
		QtCore.QMetaObject.connectSlotsByName(solicitarCartao)

	def telaComprarFichas(self):
		self.msgNovoCart.hide()
		self.solicitarCartao.hide()
		self.msgNovasFichas.show()
		self.inputFichas.show()
		self.comprarButton.show()

	def telaSolicitarCartao(self):
		if self.cliente.solcitou:
			self.msgSolCart.show()
		else:
			self.msgNovoCart.show()
			self.solicitarCartao.show()
		self.msgNovasFichas.hide()
		self.inputFichas.hide()
		self.comprarButton.hide()

	def comprarFichas(self):
		try:
			fichas = int(self.inputFichas.text());
		except:
			print('Erro2')
			return
		if fichas >= 0 and fichas <= 100:
			self.cliente.qtdFichas = banco.Banco().comprarFichas(self.cliente.qtdFichas + int(self.inputFichas.text()), self.cliente.id)
			self.numFichas.setText(QtCore.QCoreApplication.translate("solicitarCartao", str(self.cliente.qtdFichas)))
		else:
			print('Erro1')

	def solicCartao(self):
		self.cliente.solcitou = True
		self.msgNovoCart.hide()
		self.solicitarCartao.hide()
		self.msgSolCart.show()
		banco.Banco().inserirSolicitacao(self.cliente.id)

	def logout(self):
		self.tela.close()
		self.window = QtWidgets.QMainWindow()
		self.ui = login.Ui_sarulogin()
		self.ui.setupUi(self.window)
		self.window.show()

	def retranslateUi(self, solicitarCartao):
		_translate = QtCore.QCoreApplication.translate
		solicitarCartao.setWindowTitle(_translate("solicitarCartao", "Solicitar Cartão"))
		# Botão do menu de 'Comprar fichas'
		self.menuComprarButton.setText(_translate("solicitarCartao", "Comprar fichas"))
		# Botão do menu de 'Solicitar Cartão'
		self.menuSolicitarButton.setText(_translate("solicitarCartao", "Solicitar Cartão"))
		# Mensagem de Bem Vindo
		self.msgBemVindo.setText(_translate("solicitarCartao", "Bem Vindo, " + str(self.cliente.nome)))
		# Quatidade de fichas atual
		self.msgQtdFichas.setText(_translate("solicitarCartao", "Quantidade atual de fichas:"))
		# Número de fichas atuais
		self.numFichas.setText(_translate("solicitarCartao", str(self.cliente.qtdFichas)))
		# Quatidade de acesso ao RU
		self.msgQtdAcessoRU.setText(_translate("solicitarCartao", "Acessos ao Restaurante Universitário:"))
		# Número de fichas atuais
		self.numAcesso.setText(_translate("solicitarCartao", str(self.cliente.acessoRU)))
		# Label da novas fichas
		self.msgNovoCart.setText(_translate("solicitarCartao", "Ainda não possui um cartão ou perdeu o seu? Peça já!"))
		# Botão de compra
		self.solicitarCartao.setText(_translate("solicitarCartao", "Solicitar Cartão"))
		# Botão de compra
		self.comprarButton.setText(_translate("solicitarCartao", "Comprar"))
		# Label da novas fichas
		self.msgNovasFichas.setText(_translate("solicitarCartao", "Insira a quantidade de fichas que deseja comprar"))
		# Botão de sair
		self.sair.setText(_translate("solicitarCartao", "Sair"))
		# Cartão ja solicitado
		self.msgSolCart.setText(_translate("solicitarCartao", "Seu cartão já foi solicitado! Aguarde a confirmação!"))





# if __name__ == "__main__":
# 	import sys
# 	app = QtWidgets.QApplication(sys.argv)
# 	solicitarCartao = QtWidgets.QMainWindow()
# 	ui = Ui_solicitarCartao()
# 	ui.setupUi(solicitarCartao)
# 	solicitarCartao.show()
# 	sys.exit(app.exec_())