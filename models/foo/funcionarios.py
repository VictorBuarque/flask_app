from config import database

class Funcionarios(database.Model):
    __tablename__ = 'funcionarios'  # Correção do nome da tabela
    id_funcionario = database.Column(database.Integer, primary_key=True, autoincrement=True)
    nome_funcionario = database.Column(database.String(75), nullable=False)
    cpf_funcionario = database.Column(database.String(14), nullable=False)
    email_funcionario = database.Column(database.String(100), nullable=False)
    
    def __init__(self, nome, cpf, email):
        self.nome_funcionario = nome
        self.cpf_funcionario = cpf
        self.email_funcionario = email
