import datetime
import os
import psycopg2

class Banco:
	def __init__(self):
		try:
			self.DATABASE_URL = 'postgres://lbhulooslrsocn:be3ec9a09747fb838a553d044e914636d6e348fe1cddea874558d8e737f11edf@ec2-23-23-80-20.compute-1.amazonaws.com:5432/dsqk3gs6dme27'
			self.conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')
			self.conn.autocommit = True
			self.cursor = self.conn.cursor()
		except psycopg2.Error as e:
			print('Não foi possivel conectar no banco de dados!')
			print(e)

	def inserirSolicitacao(self, id):
		query = ("INSERT INTO solicitacao (data_pedido, data_entrega, usuario_id, atendido) VALUES (%s, %s, %s, %s)")
		data = datetime.datetime.now()
		data = datetime.datetime.date(data)
		data1 = datetime.date(2000, 1, 1)
		dados = (data, data1, id, 0)
		try:
			self.cursor.execute(query, dados)
		except Exception as e:
			print(e)

	def comprarFichas(self, fichas, id):
		query = ("UPDATE usuario SET tickets = %s WHERE id = %s")
		dados = (fichas, id)
		self.cursor.execute(query, dados)
		query = ("SELECT tickets FROM usuario WHERE id = '{}'").format(id)
		self.cursor.execute(query)
		try:
			temp = self.cursor.fetchone()[0]
			return temp
		except Exception as e:
			print(e)
			return False

	def logar(self, login, senha):
		query = ("SELECT id, nome, tickets, quantidade_acessos FROM usuario WHERE username = %s AND senha = %s")
		self.cursor.execute(query, (login, senha))
		try:
			temp = self.cursor.fetchone()
			return temp
		except:
			return False

	def logarAdm(self, login, senha):
		query = ("SELECT id FROM admin WHERE login = %s AND senha = %s")
		self.cursor.execute(query, (login, senha))
		try:
			temp = self.cursor.fetchone()[0]
			return temp
		except:
			return False

	def cadastrar(self, id, dados):
		query = ("UPDATE usuario SET nome = %s, sobrenome = %s, cpf = %s, curso = %s, campus = %s, senha = %s, username = %s, Cartao_id = %s WHERE id = %s")
		dados = (dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], id)
		self.cursor.execute(query, dados)

	def buscarSolicitacoes(self):
		query = ("SELECT id, data_pedido, usuario_id FROM solicitacao WHERE atendido = 0")
		self.cursor.execute(query, ())
		try:
			temp = self.cursor.fetchall()
			return temp
		except:
			return False

	def excluirSolicitacao(self, id):
		query =  ("UPDATE solicitacao SET atendido = 1 WHERE id = {}").format(id)
		self.cursor.execute(query)

	def solicitou(self, id):
		query = ("SELECT id FROM solicitacao WHERE usuario_id = {} AND atendido = 0").format(id)
		self.cursor.execute(query)
		try:
			temp = self.cursor.fetchone()[0]
			return temp
		except:
			return False

	def dadosUsuario(self, matricula):
		query = ("SELECT id, nome, sobrenome, cpf, curso, campus FROM usuario WHERE matricula = '{}'").format(matricula)
		self.cursor.execute(query)
		try:
			temp = self.cursor.fetchone()
			return temp
		except:
			return False

	def buscaIdCartao(self):
		query = ("SELECT cartao.id FROM cartao FULL OUTER JOIN usuario ON cartao.id = usuario.cartao_id WHERE cartao.id IS NULL OR usuario.id IS NULL ORDER BY cast(cartao.id as int)")
		self.cursor.execute(query)
		try:
			temp = self.cursor.fetchone()[0]
			return temp
		except:
			return False

	def buscarCartao(self, numCartao):
		query = ("SELECT id, nome, tickets, quantidade_acessos FROM usuario WHERE cartao_id = '{}'").format(numCartao)
		self.cursor.execute(query)
		try:
			temp = self.cursor.fetchone()
			return temp
		except:
			return False

	def atualizarNumDeFichas(self, id, tickets, quantidade_acessos):
		query = ("UPDATE usuario SET tickets = %s, quantidade_acessos = %s WHERE id = %s")
		dados = (tickets, quantidade_acessos, id)
		self.cursor.execute(query, dados)