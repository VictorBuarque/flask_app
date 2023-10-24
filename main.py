from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/crm_victor'

db = SQLAlchemy(app)

class Clientes(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cliente = db.Column(db.String(75), nullable=False)
    cpf_cliente = db.Column(db.String(14), nullable=False)
    email_cliente = db.Column(db.String(100), nullable=False)
    
    def __init__(self, nome, cpf, email):
        self.nome_cliente = nome
        self.cpf_cliente = cpf
        self.email_cliente = email

@app.route("/")
def database():
    clientes = Clientes.query.all()
    return render_template('index.html', clientes=clientes)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        clientes = Clientes(nome, cpf, email)
        db.session.add(clientes)
        db.session.commit()
        return redirect(url_for('database'))
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)
