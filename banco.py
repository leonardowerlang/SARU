from mysql.connector import errorcode
from datetime import datetime
import mysql.connector

class Banco:
	def __init__(self):
		try:
			self.cnx = mysql.connector.connect(user='root', password='', host='localhost', database='id7771447_saru')
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)

	def inserirSolicitacao(self, id):
		query = ("INSERT INTO solicitacao (data_pedido, Usuario_id, atendido) VALUES (%s, %s, %s)")
		data = datetime.now()
		data = datetime.date(data)
		dados = (data, id, 0)
		cursor = self.cnx.cursor()
		cursor.execute(query, dados)
		self.cnx.commit()
		cursor.close()
		self.close()

	def comprarFichas(self, fichas, id):
		query = ("UPDATE usuario SET tickets = %s WHERE id = %s")
		dados = (fichas, id)
		cursor = self.cnx.cursor()
		cursor.execute(query, dados)
		self.cnx.commit()
		query = ("SELECT tickets FROM usuario WHERE id = '{}'").format(id)
		cursor.execute(query)
		for i in cursor:
			return i[0]
		self.close()
		return False

	def logar(self, login, senha):
		cursor = self.cnx.cursor()
		query = ("SELECT id, nome, tickets, quantidade_acessos FROM usuario WHERE username = %s AND senha = %s")
		cursor.execute(query, (login, senha))
		for i in cursor:
			return i
		cursor.close()
		self.close()
		return False

	def logarAdm(self, login, senha):
		cursor = self.cnx.cursor()
		query = ("SELECT id FROM admin WHERE login = %s AND senha = %s")
		cursor.execute(query, (login, senha))
		for i in cursor:
			return i
		cursor.close()
		self.close()
		return False

	def cadastrar(self, dados):
		cursor = self.cnx.cursor()
		query = ("INSERT INTO usuario (nome, sobrenome, matricula, cpf, curso, campus, senha, username, quantidade_acessos, tickets) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
		dados = (dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], 0, 0)
		cursor.execute(query, dados)
		self.cnx.commit()
		cursor.close()
		self.close()

	def buscarSolicitacoes(self):
		cursor = self.cnx.cursor()
		query = ("SELECT id, data_pedido, Usuario_id FROM solicitacao")
		cursor.execute(query, ())
		temp = []
		for i in cursor:
			temp.append(i)
		cursor.close()
		self.close()
		return temp

	def excluirSolicitacao(self, id):
		cursor = self.cnx.cursor()
		query =  ("DELETE FROM solicitacao WHERE Usuario_id = {}").format(id)
		cursor.execute(query)
		cursor.close()
		self.cnx.commit()
		self.close

	def solicitou(self, id):
		cursor = self.cnx.cursor()
		query = ("SELECT id FROM solicitacao WHERE Usuario_id = {}").format(id)
		cursor.execute(query)
		for i in cursor:
			return True
		cursor.close()
		self.close
		return False

	def close(self):
		self.cnx.close()