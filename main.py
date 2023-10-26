from flask import Flask, render_template, request, redirect, url_for
from config import app_config, database
from models.foo.clientes import Clientes
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)
# Configuração do flask
app.config.from_object(app_config['development'])
database.init_app(app)

# Cria a engine do banco
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Cria a sessão obrigatório a partir do SQLALCHEMY2.0
Session = sessionmaker(bind=engine)

#Index
@app.route("/")
def home():
    session = Session()
    clientes = session.query(Clientes).all()
    session.close()
    return render_template('index.html', clientes=clientes)

#cadastrarclientes
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        session = Session()
        cliente = Clientes(nome=nome, cpf=cpf, email=email)
        session.add(cliente)
        session.commit()
        session.close()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/delete/<int:id>")
def delete(id):
    session = Session()
    cliente = session.query(Clientes).get(id)
    session.delete(cliente)
    session.commit()
    return redirect(url_for('home'))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    session = Session()
    cliente = session.query(Clientes).get(id)

    if not cliente:
        session.close()
        return "Cliente not found"

    if request.method == "POST":
        try:
            nome = request.form['nome']
            cpf = request.form['cpf']
            email = request.form['email']

            # Atualiza os objetos na classe cliente
            cliente.nome_cliente = nome
            cliente.cpf_cliente = cpf
            cliente.email_cliente = email
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()
            return redirect(url_for('home'))
    return render_template('edit.html', cliente=cliente)


if __name__ == "__main__":
    app.run(debug=True)
