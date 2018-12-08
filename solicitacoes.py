# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solicitacoes.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import admin
import banco

class Ui_Solicitacao(object):
    def setupUi(self, Solicitacao):
        self.tela = Solicitacao
        Solicitacao.setObjectName("Solicitacao")
        Solicitacao.resize(800, 600)
        Solicitacao.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.listWidget = QtWidgets.QListWidget(Solicitacao)
        self.listWidget.setGeometry(QtCore.QRect(25, 60, 750, 480))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(False)
        item.setFont(font)

        temp = banco.Banco().buscarSolicitacoes()
        cont = 0
        for i in temp:
            self.listWidget.addItem(item)
            item = QtWidgets.QListWidgetItem()
            texto = self.listWidget.item(cont)
            texto.setText(QtCore.QCoreApplication.translate("Solicitacao", "ID Usuario: " + str(i[2]) + " \t\t\tData de Solicitação: " + str(i[1])))
            cont += 1


        self.delete_2 = QtWidgets.QPushButton(Solicitacao)
        self.delete_2.setGeometry(QtCore.QRect(40, 545, 160, 25))
        self.delete_2.setObjectName("delete_2")
        self.delete_2.clicked.connect(self.excluirSolicitacao)

        self.cancel = QtWidgets.QPushButton(Solicitacao)
        self.cancel.setGeometry(QtCore.QRect(565, 545, 160, 25))
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(self.voltar)

        self.label_5 = QtWidgets.QLabel(Solicitacao)
        self.label_5.setGeometry(QtCore.QRect(40, 20, 301, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Solicitacao)
        QtCore.QMetaObject.connectSlotsByName(Solicitacao)

    def excluirSolicitacao(self):
        print(self.listWidget.currentRow())
        if self.listWidget.currentRow() >= 0:
            item = self.listWidget.takeItem(self.listWidget.currentRow())
            temp = item.text().split(' ')
            banco.Banco().excluirSolicitacao(temp[2])

    def voltar(self):
        self.tela.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = admin.Ui_Home()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, Solicitacao):
        _translate = QtCore.QCoreApplication.translate
        Solicitacao.setWindowTitle(_translate("Solicitacao", "Solicitações"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(1)

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.delete_2.setText(_translate("Solicitacao", "Excluir solicitação"))
        self.cancel.setText(_translate("Solicitacao", "Voltar"))
        self.label_5.setText(_translate("Solicitacao", "Solicitações de cadastro de usuário"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Solicitacao = QtWidgets.QDialog()
#     ui = Ui_Solicitacao()
#     ui.setupUi(Solicitacao)
#     Solicitacao.show()
#     sys.exit(app.exec_())