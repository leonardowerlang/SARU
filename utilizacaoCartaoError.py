# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_utilizacaoCartaoErro(object):
	def setupUi(self, utilizacaoCartaoErro):
		utilizacaoCartaoErro.setObjectName("utilizacaoCartaoErro")
		utilizacaoCartaoErro.resize(480, 135)
		icon = QtGui.QIcon.fromTheme("SARU")
		utilizacaoCartaoErro.setWindowIcon(icon)
		utilizacaoCartaoErro.setStyleSheet("background-color: rgb(247, 247, 247);")
		self.pushButton_2 = QtWidgets.QPushButton(utilizacaoCartaoErro)
		self.pushButton_2.setGeometry(QtCore.QRect(165, 80, 141, 41))
		self.pushButton_2.setObjectName("pushButton_2")
		self.labelNome = QtWidgets.QLabel(utilizacaoCartaoErro)
		self.labelNome.setGeometry(QtCore.QRect(30, 30, 480, 31))
		self.labelNome.setMaximumSize(QtCore.QSize(480, 31))
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

		self.retranslateUi(utilizacaoCartaoErro)
		QtCore.QMetaObject.connectSlotsByName(utilizacaoCartaoErro)

	def retranslateUi(self, utilizacaoCartaoErro):
		_translate = QtCore.QCoreApplication.translate
		utilizacaoCartaoErro.setWindowTitle(_translate("utilizacaoCartaoErro", "Erro"))
		self.pushButton_2.setText(_translate("utilizacaoCartaoErro", "Sair"))
		self.labelNome.setText(_translate("utilizacaoCartaoErro", "Erro na hora de identificar o cartão!"))

import logo_rc

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	utilizacaoCartaoErro = QtWidgets.QDialog()
	ui = Ui_utilizacaoCartaoErro()
	ui.setupUi(utilizacaoCartaoErro)
	utilizacaoCartaoErro.show()
	sys.exit(app.exec_())

