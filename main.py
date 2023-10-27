from flask import Flask, render_template, request, redirect, url_for
from config import app_config, database
from models.foo.clientes import Clientes
from models.foo.funcionarios import Funcionarios

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
    funcionarios = session.query(Funcionarios).all()
    session.close()
    return render_template('index.html', clientes=clientes, funcionarios=funcionarios)

#cadastrar clientes
@app.route("/add_cliente", methods=["GET", "POST"])
def add_cliente():
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
    return render_template('add_cliente.html')

#cadastrar funcionario
@app.route("/add_funcionario", methods=["GET", "POST"])
def add_funcionario():
    if request.method == "POST":
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        session = Session()
        funcionarios = Funcionarios(nome=nome, cpf=cpf, email=email)
        session.add(funcionarios)
        session.commit()
        session.close()
        return redirect(url_for('home'))
    return render_template('add_funcionario.html')


@app.route("/delete_cliente/<int:id>")
def delete_cliente(id):
    session = Session()
    cliente = session.query(Clientes).get(id)
    if cliente:
        session.delete(cliente)
        session.commit()
    
    session.close()
    return redirect(url_for('home'))

@app.route("/delete_funcionario/<int:id>")
def delete_funcionario(id):
    session = Session()
    funcionario = session.query(Funcionarios).get(id)
    if funcionario:
        session.delete(funcionario)
        session.commit()
    
    session.close()
    return redirect(url_for('home'))



@app.route("/edit_cliente/<int:id>", methods=["GET", "POST"])
def edit_cliente(id):
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
    
    return render_template('edit_cliente.html', cliente=cliente)

@app.route("/edit_funcionario/<int:id>", methods=["GET", "POST"])
def edit_funcionario(id):
    session = Session()
    funcionario = session.query(Funcionarios).get(id)

    if not funcionario:
        session.close()
        return "Funcionário not found"

    if request.method == "POST":
        try:
            nome = request.form['nome']
            cpf = request.form['cpf']
            email = request.form['email']

            # Atualiza os objetos na classe funcionario
            funcionario.nome_funcionario = nome
            funcionario.cpf_funcionario = cpf
            funcionario.email_funcionario = email
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()
            return redirect(url_for('home'))
    
    return render_template('edit_funcionario.html', funcionario=funcionario)



if __name__ == "__main__":
    app.run(debug=True)
