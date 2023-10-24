from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Clientes(db.Model):
    __tablename__ = 'clientes'  # Correção do nome da tabela
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cliente = db.Column(db.String(75), nullable=False)
    cpf_cliente = db.Column(db.String(14), nullable=False)
    email_cliente = db.Column(db.String(100), nullable=False)
    
    def __init__(self, nome, cpf, email):
        self.nome_cliente = nome
        self.cpf_cliente = cpf
        self.email_cliente = email
