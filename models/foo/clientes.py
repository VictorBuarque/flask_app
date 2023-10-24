from flask_sqlalchemy import SQLAlchemy
from config import database
class Clientes(database.Model):
    __tablename__ = 'clientes'  # Correção do nome da tabela
    id_cliente = database.Column(database.Integer, primary_key=True, autoincrement=True)
    nome_cliente = database.Column(database.String(75), nullable=False)
    cpf_cliente = database.Column(database.String(14), nullable=False)
    email_cliente = database.Column(database.String(100), nullable=False)
    
    def __init__(self, nome, cpf, email):
        self.nome_cliente = nome
        self.cpf_cliente = cpf
        self.email_cliente = email
