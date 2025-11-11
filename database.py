import mysql.connector


def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        username="root",
        password="root",
        database="sistema_gerenciamento"
    )