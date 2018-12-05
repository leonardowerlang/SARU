# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_vendaTicketsErro(object):
	def setupUi(self, vendaTicketsErro):
		vendaTicketsErro.setObjectName("vendaTicketsErro")
		vendaTicketsErro.resize(480, 135)
		icon = QtGui.QIcon.fromTheme("SARU")
		vendaTicketsErro.setWindowIcon(icon)
		vendaTicketsErro.setStyleSheet("background-color: rgb(247, 247, 247);")
		self.pushButton_2 = QtWidgets.QPushButton(vendaTicketsErro)
		self.pushButton_2.setGeometry(QtCore.QRect(165, 80, 141, 41))
		self.pushButton_2.setObjectName("pushButton_2")
		self.labelNome = QtWidgets.QLabel(vendaTicketsErro)
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

		self.retranslateUi(vendaTicketsErro)
		QtCore.QMetaObject.connectSlotsByName(vendaTicketsErro)

	def retranslateUi(self, vendaTicketsErro):
		_translate = QtCore.QCoreApplication.translate
		vendaTicketsErro.setWindowTitle(_translate("vendaTicketsErro", "Erro"))
		self.pushButton_2.setText(_translate("vendaTicketsErro", "Sair"))
		self.labelNome.setText(_translate("vendaTicketsErro", "Erro na hora de comprar os tickets!"))

import logo_rc

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	vendaTicketsErro = QtWidgets.QDialog()
	ui = Ui_vendaTicketsErro()
	ui.setupUi(vendaTicketsErro)
	vendaTicketsErro.show()
	sys.exit(app.exec_())

