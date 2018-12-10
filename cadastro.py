# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib
import banco
import admin
import erro

class Ui_Form(object):
    def setupUi(self, Form):
        self.tela = Form
        self.idUsuario = -1
        Form.setObjectName("Form")
        Form.resize(708, 418)
        Form.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.graphicsViewFoto = QtWidgets.QGraphicsView(Form)
        self.graphicsViewFoto.setGeometry(QtCore.QRect(490, 70, 171, 192))
        self.graphicsViewFoto.setObjectName("graphicsViewFoto")
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 51, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(170, 30, 241, 19))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.lineEditMatricula = QtWidgets.QLineEdit(Form)
        self.lineEditMatricula.setGeometry(QtCore.QRect(140, 70, 301, 27))
        self.lineEditMatricula.setText("")
        self.lineEditMatricula.setObjectName("lineEditMatricula")
        self.labelMatricula = QtWidgets.QLabel(Form)
        self.labelMatricula.setGeometry(QtCore.QRect(67, 66, 70, 31))
        self.labelMatricula.setObjectName("labelMatricula")

        self.lineEditNome = QtWidgets.QLineEdit(Form)
        self.lineEditNome.setGeometry(QtCore.QRect(140, 100, 301, 27))
        self.lineEditNome.setText("")
        self.lineEditNome.setObjectName("lineEditNome")
        self.lineEditNome.setEnabled(False)
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setGeometry(QtCore.QRect(90, 96, 45, 31))
        self.labelNome.setObjectName("labelNome")

        self.lineEditSobrenome = QtWidgets.QLineEdit(Form)
        self.lineEditSobrenome.setGeometry(QtCore.QRect(140, 130, 301, 27))
        self.lineEditSobrenome.setText("")
        self.lineEditSobrenome.setObjectName("lineEditSobrenome")
        self.lineEditSobrenome.setEnabled(False)
        self.labelSobrenome = QtWidgets.QLabel(Form)
        self.labelSobrenome.setGeometry(QtCore.QRect(53, 126, 82, 31)) # pos X, Y tam Y , X
        self.labelSobrenome.setObjectName("labelSobrenome")

        self.lineEditCPF = QtWidgets.QLineEdit(Form)
        self.lineEditCPF.setGeometry(QtCore.QRect(140, 160, 301, 27))
        self.lineEditCPF.setObjectName("lineEditCPF")
        self.lineEditCPF.setEnabled(False)
        self.labelCPF = QtWidgets.QLabel(Form)
        self.labelCPF.setGeometry(QtCore.QRect(105, 159, 30, 21))
        self.labelCPF.setObjectName("labelCPF")

        self.lineEditCurso = QtWidgets.QLineEdit(Form)
        self.lineEditCurso.setGeometry(QtCore.QRect(140, 190, 301, 27))
        self.lineEditCurso.setObjectName("lineEditCurso")
        self.lineEditCurso.setEnabled(False)
        self.labelCurso = QtWidgets.QLabel(Form)
        self.labelCurso.setGeometry(QtCore.QRect(91, 190, 42, 21))
        self.labelCurso.setObjectName("labelCurso")

        self.lineEditCampus = QtWidgets.QLineEdit(Form)
        self.lineEditCampus.setGeometry(QtCore.QRect(140, 220, 301, 27))
        self.lineEditCampus.setObjectName("lineEditCampus")
        self.lineEditCampus.setEnabled(False)
        self.labelCampus = QtWidgets.QLabel(Form)
        self.labelCampus.setGeometry(QtCore.QRect(76, 220, 57, 21))
        self.labelCampus.setObjectName("labelCampus")

        self.usuario = QtWidgets.QLineEdit(Form)
        self.usuario.setGeometry(QtCore.QRect(140, 250, 301, 27))
        self.usuario.setObjectName("usuario")
        self.usuario.setEnabled(False)
        self.labelUsuario = QtWidgets.QLabel(Form)
        self.labelUsuario.setGeometry(QtCore.QRect(77, 253, 55, 16))
        self.labelUsuario.setObjectName("labelUsuario")

        self.senha = QtWidgets.QLineEdit(Form)
        self.senha.setGeometry(QtCore.QRect(140, 280, 301, 27))
        self.senha.setObjectName("senha")
        self.senha.setEnabled(False)
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.labelSenha = QtWidgets.QLabel(Form)
        self.labelSenha.setGeometry(QtCore.QRect(88, 283, 50, 16))
        self.labelSenha.setObjectName("labelSenha")

        self.confirmarSenha = QtWidgets.QLineEdit(Form)
        self.confirmarSenha.setGeometry(QtCore.QRect(140, 310, 301, 27))
        self.confirmarSenha.setObjectName("confirmarSenha")
        self.confirmarSenha.setEnabled(False)
        self.confirmarSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.labelConfSenha = QtWidgets.QLabel(Form)
        self.labelConfSenha.setGeometry(QtCore.QRect(16, 313, 118, 16))
        self.labelConfSenha.setObjectName("labelConfSenha")

        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText('')
        self.lineEdit.setGeometry(QtCore.QRect(140, 340, 301, 25))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(65, 343, 70, 16))
        self.label.setObjectName("label")

        self.btnOk = QtWidgets.QPushButton(Form)
        self.btnOk.setGeometry(QtCore.QRect(140, 380, 150, 27))
        self.btnOk.setStyleSheet("background-color: rgb(63, 114, 105);")
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(self.procurarDados)

        self.btnCadastrar = QtWidgets.QPushButton(Form)
        self.btnCadastrar.setGeometry(QtCore.QRect(140, 380, 150, 27))
        self.btnCadastrar.setStyleSheet("background-color: rgb(63, 114, 105);")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.btnCadastrar.hide()
        self.btnCadastrar.clicked.connect(self.cadastrar)

        self.btnCancelar = QtWidgets.QPushButton(Form)
        self.btnCancelar.setGeometry(QtCore.QRect(291, 380, 150, 27))
        self.btnCancelar.setStyleSheet("background-color: rgb(63, 114, 105);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnCancelar.clicked.connect(self.cancelarCadastro)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def procurarDados(self):
        try:
            matricula = (int(self.lineEditMatricula.text()))
        except:
            self.window = QtWidgets.QMainWindow()
            self.ui = erro.Ui_cadastroJaExiste()
            self.ui.setupUi(self.window, "Dados informados incorretamente!")
            self.window.show()
            return
        temp = banco.Banco().dadosUsuario(matricula)
        idCartao = banco.Banco().buscaIdCartao()
        if idCartao:
            if temp:
                self.idUsuario = temp[0]
                self.lineEditMatricula.setEnabled(False)
                self.lineEditNome.setText(temp[1])
                self.lineEditSobrenome.setText(temp[2])
                self.lineEditCPF.setText(temp[3])
                self.lineEditCurso.setText(temp[4])
                self.lineEditCampus.setText(temp[5])
                self.usuario.setText((str(temp[1]) + '.' + str(temp[2])).lower().replace(' ', ''))
                self.lineEdit.setText(idCartao)
                self.usuario.setEnabled(True)
                self.senha.setEnabled(True)
                self.confirmarSenha.setEnabled(True)
                self.btnOk.hide()
                self.btnCadastrar.show()
            else:
                self.idUsuario = -1
                self.window = QtWidgets.QMainWindow()
                self.ui = erro.Ui_cadastroJaExiste()
                self.ui.setupUi(self.window, "Usuário não encontrado!")
                self.window.show()
        else:
            self.idUsuario = -1
            self.window = QtWidgets.QMainWindow()
            self.ui = erro.Ui_cadastroJaExiste()
            self.ui.setupUi(self.window, "Não existem mais cartões disponiveis!")
            self.window.show()

    def cadastrar(self):
        temp = []
        temp.append(self.lineEditNome.text())
        temp.append(self.lineEditSobrenome.text())
        temp.append(self.lineEditCPF.text())
        temp.append(self.lineEditCurso.text())
        temp.append(self.lineEditCampus.text())
        if self.senha.text() == self.confirmarSenha.text():
            h = hashlib.sha1()
            h.update((self.senha.text()).encode('utf-8'))
            temp.append(h.hexdigest())
        else:
            print('Senha incorretas')
            return
        temp.append(self.usuario.text())
        try:
            temp.append(int(self.lineEdit.text()))
        except:
            self.window = QtWidgets.QMainWindow()
            self.ui = erro.Ui_cadastroJaExiste()
            self.ui.setupUi(self.window, "Dados informados incorretamente!")
            self.window.show()
            return
        banco.Banco().cadastrar(self.idUsuario, temp)
        self.tela.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = admin.Ui_Home()
        self.ui.setupUi(self.window)
        self.window.show()

    def cancelarCadastro(self):
        self.tela.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = admin.Ui_Home()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro da Matrícula"))
        self.labelMatricula.setText(_translate("Form", "Matricula:"))
        self.labelCPF.setText(_translate("Form", "CPF:"))
        self.labelCampus.setText(_translate("Form", "Campus:"))
        self.labelCurso.setText(_translate("Form", "Curso:"))
        self.labelNome.setText(_translate("Form", "Nome:"))
        self.labelSobrenome.setText(_translate("Form", "Sobrenome:"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><img src=\"logo.png\"/></p></body></html>"))
        self.label_5.setText(_translate("Form", "Vinculação da Matrícula"))
        self.label.setText(_translate("Form", "ID Cartão:"))
        self.labelSenha.setText(_translate("Form", "Senha:"))
        self.labelUsuario.setText(_translate("Form", "Usuario:"))
        self.labelConfSenha.setText(_translate("Form", "Confirmar Senha:"))
        self.btnOk.setText(_translate("Form", "Procurar Matricula"))
        self.btnCadastrar.setText(_translate("Form", "Finalizar Cadastro"))
        self.btnCancelar.setText(_translate("Form", "Cancelar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Solicitacao = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Solicitacao)
    Solicitacao.show()
    sys.exit(app.exec_())