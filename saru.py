from PyQt5 import QtCore, QtGui, QtWidgets
import solicitarCartao
import login
import banco
import time
import sys

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	sarulogin = QtWidgets.QMainWindow()
	ui = login.Ui_sarulogin()
	ui.setupUi(sarulogin)
	sarulogin.show()
	app.exec_()