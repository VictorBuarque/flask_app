from flask import Flask, render_template, request, redirect, url_for
from config import app_config, database
from models.foo.clientes import Clientes

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    database.init_app(app)
    return app

app = create_app('development')
with app.app_context():
    database.create_all()

@app.route("/")
def home():
    clientes = Clientes.query.all()
    return render_template('index.html', clientes=clientes)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        cliente = Clientes(nome, cpf, email)
        database.session.add(cliente)
        database.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/delete/<int:id>")
def delete(id):
    cliente = Clientes.query.get(id)
    database.session.delete(cliente)
    database.session.commit()
    return redirect(url_for('home'))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cliente = Clientes.query.get(id)
    if request.method == "POST":
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        cliente.nome_cliente = nome
        cliente.cpf_cliente = cpf
        cliente.email_cliente = email
        database.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', cliente=cliente)

if __name__ == "__main__":
    app.run(debug=True)
