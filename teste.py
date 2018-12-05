# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class App(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo de Avançar e Retroceder")
        self.setGeometry(100, 100, 500, 300)

        windowLayout = QGridLayout()
        self.setLayout(windowLayout)

        self.Lista_de_exibicao = []

        """
        self.Lista_de_exibicao: Terá os Widgets que serão ora mostrados, ora ocultados
        Atenção: caso seja mais conveniente, em vez de array, pode ser usado um dicionário.
        """
        self.PosAtual = 0              # Index do Item que está sendo mostrado


        nome = self.criaNome()
        windowLayout.addWidget(nome, 0, 0, 1, 2, Qt.AlignTop)
        self.Lista_de_exibicao.append(nome)

        parceiro = self.criaPrarceiro()
        windowLayout.addWidget(parceiro, 1, 0, 1, 2, Qt.AlignTop)
        self.Lista_de_exibicao.append(parceiro)

        lazer = self.criaLazer()
        windowLayout.addWidget(lazer, 2, 0, 1, 2, Qt.AlignTop)
        self.Lista_de_exibicao.append(lazer)

        transporte = self.criaTransporte()
        windowLayout.addWidget(transporte, 3, 0, 1, 2, Qt.AlignTop)
        self.Lista_de_exibicao.append(transporte)

        veiculo = self.criaVeiculo()
        windowLayout.addWidget(veiculo, 4, 0, 1, 2)
        self.Lista_de_exibicao.append(veiculo)


        respostas = self.criaRespostas()
        windowLayout.addWidget(respostas, 5, 0, 1, 2)
        self.Lista_de_exibicao.append(respostas)

        self.btn_anterior = QPushButton(" < Anterior ")
        self.btn_anterior.step_value = -1  # O step_value = -1 leva ao índice anterior
        self.btn_anterior.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.btn_anterior.hide()
        self.btn_anterior.clicked.connect(self.buttonClick)  # Os DOIS BOTÕES usam o mesmo slot!

        self.btn_proximo = QPushButton("  Próxima  > ")
        self.btn_proximo.step_value = 1  # O step_value = 1  leva ao próximo índice
        self.btn_proximo.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.btn_proximo.clicked.connect(self.buttonClick)  # Os DOIS BOTÕES usam o mesmo slot!

        self.btn_sair = QPushButton("Sair")
        self.btn_sair.hide()
        self.btn_sair.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.btn_sair.clicked.connect(QCoreApplication.instance().quit)

        FrameBtns = QFrame()
        layout_frame_btns = QHBoxLayout()
        FrameBtns.setLayout(layout_frame_btns)
        layout_frame_btns.addWidget(self.btn_anterior)
        layout_frame_btns.addWidget(self.btn_proximo)
        layout_frame_btns.addWidget(self.btn_sair)

        windowLayout.addWidget(FrameBtns, 6, 1, 1, 1, Qt.AlignBottom)

        self.show()

    def criaNome(self):
        GNome = QGroupBox("Nome")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Qual seu nome?"))
        self.nome = QLineEdit()       # sempre colocando no self aqueles que precisará chamar no futuro
        layout.addWidget(self.nome)
        GNome.setLayout(layout)
        return GNome

    def criaPrarceiro(self):
        self.GParceiro = QGroupBox("Parceiro(a) ideal para você")
        layout = QVBoxLayout()
        layout.addWidget(QRadioButton("Loiro(a)"))
        layout.addWidget(QRadioButton("Moreno(a)"))
        layout.addWidget(QRadioButton("Ruivo(a)"))
        layout.addWidget(QRadioButton("Mulato(a)"))
        layout.addWidget(QRadioButton("Negro(a)"))
        layout.addWidget(QRadioButton("Indígena"))
        layout.addWidget(QRadioButton("Isso não é relevante"))
        self.GParceiro.setLayout(layout)
        self.GParceiro.hide()
        return self.GParceiro

    def criaLazer(self):
        self.GLazer = QGroupBox("Lazer")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("O que você gosta de fazer?"))
        layout.addWidget(QCheckBox("Esportes coletivos(futebol, vôlei, basquete, ...)"))
        layout.addWidget(QCheckBox("Esportes individuais(tênis, boliche, badminton,...)"))
        layout.addWidget(QCheckBox("Esportes radicais(paraquedismo, automobilismo, motocross,...)"))
        layout.addWidget(QCheckBox("Artes marciais(judô, taekwondo, jiu-jitsu,...)"))
        layout.addWidget(QCheckBox("Escotismo, acampamento, pescaria, ..."))
        layout.addWidget(QCheckBox("Hobby(fazer móveis, artesanato, desenho, pintura,...)"))
        layout.addWidget(QCheckBox("Atividades gamer, e-sports,...)"))
        self.GLazer.setLayout(layout)
        self.GLazer.hide()
        return self.GLazer

    def criaTransporte(self):
        self.GTransporte = QGroupBox("Qual seu meio de transporte preferido?")
        layout = QVBoxLayout()
        layout.addWidget(QRadioButton("Avião"))
        layout.addWidget(QRadioButton("Carro"))
        layout.addWidget(QRadioButton("Moto"))
        layout.addWidget(QRadioButton("Barco"))
        layout.addWidget(QRadioButton("Bicicleta"))
        self.GTransporte.setLayout(layout)
        self.GTransporte.hide()
        return self.GTransporte

    def criaVeiculo(self):
        GVeiculo = QGroupBox("Descreva como você considera que seria seu veículo ideal")
        layout = QVBoxLayout()
        self.about_veic = QPlainTextEdit()
        layout.addWidget(self.about_veic)
        GVeiculo.setLayout(layout)
        GVeiculo.hide()
        return GVeiculo

    def criaRespostas(self):
        GResposta = QGroupBox("Obtenção dos dados")
        layout = QVBoxLayout()
        self.browser = QTextBrowser()
        layout.addWidget(self.browser)
        GResposta.setLayout(layout)
        GResposta.hide()
        return GResposta

    # O dois botão usam o mesmo slot buttonClic e avançando ou retornando,
    # dependo do valor do self.sender().step_value ==> 1: "Próximo", -1:"Anterior"
    def buttonClick(self):
        MaxIndex = len(self.Lista_de_exibicao) - 1

        self.Lista_de_exibicao[self.PosAtual].hide()

        if self.PosAtual == MaxIndex:
            self.btn_sair.hide()
            self.btn_proximo.show()

        self.PosAtual += self.sender().step_value     # Atualiza o indice
        self.Lista_de_exibicao[self.PosAtual].show()  # Mostra o próximo grupo items (anterior ou posterior!)

        if self.PosAtual == MaxIndex - 1:
            self.btn_proximo.setText("Finalizar")
        elif self.PosAtual == MaxIndex - 2:
            self.btn_proximo.setText("Avançar > ")
        elif self.PosAtual == MaxIndex:
            self.btn_proximo.hide()
            self.btn_sair.show()

            # Busca dos dados
            self.browser.clear()
            html = "<big><b>Suas respostas Foram</b></big><br>"

            texto = self.nome.text()
            if len(texto) > 0:
                html += "Nome: <big><i><font color = blue>"
                html +=  texto + "</font></i></big><br>"
            else:
                html += "Você não respondeu qual é o seu nome!<br>"

            ParCh = self.GParceiro.children()
            parc = ""
            for ch in ParCh:
                if isinstance(ch, QRadioButton):
                    if ch.isChecked():
                        parc = ch.text()
            if len(parc) > 0:
                html += "Parceiro(a) ideal: <big><i><font color = blue>"
                html += parc + "</font></i></big><br>"
            else:
                html += "Você não disse qual o seu tipo preferido de parceiro!<br>"

            LazerCh = self.GLazer.children()
            lazer = ""
            for lz in LazerCh:
                if isinstance(lz, QCheckBox):
                    if lz.isChecked():
                        lazer += lz.text() + "<br>"
            if len(lazer) > 0:
                html += "Sobre Lazer, você disse que gosta de: <br><big><i><font color = blue>"
                html += lazer + "<br></font></i></big>"
            else:
                html += "Não foi marcada nenhuma opção de lazer.<br>"

            TransCh = self.GTransporte.children()
            transp = ""
            for tr in TransCh:
                if isinstance(tr, QRadioButton):
                    if tr.isChecked():
                        transp += tr.text() + "<br>"
            if len(transp) > 0:
                html += "Transporte preferido : <big><i><font color = blue>"
                html += transp + "</font></i></big><br>"
            else:
                html += "Não foi marcada a opção de transporte preferido.<br>"

            abveic = self.about_veic.toPlainText()
            if len(abveic) > 0:
                html += "Considerações sobre su veículo ideal: <big><i><font color = blue>"
                html +=  abveic + "</font></i></big><br>"
            else:
                html += "Não foi feita nenhuma consideração a respeito de como seria o seu veículo ideal."

            self.browser.setHtml(html)

        elif self.PosAtual == 0:
            self.btn_anterior.hide()
        elif self.PosAtual == 1:
            self.btn_anterior.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())