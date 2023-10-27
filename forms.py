from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class FormFuncionario(FlaskForm):
    id_funcionario = StringField('Identificador')
    nome_funcionario = StringField('Nome',validators=[DataRequired()])
    telefone_cliente = StringField('celular',validators=[DataRequired()])
    email_cliente = StringField('e-mail',validators=[DataRequired(),Email()])
    senha_cliente = StringField('Senha',validators=[DataRequired(),Length(6,16)])
    confirma_senha = StringField('Confirmação Senha',validators=[DataRequired(),EqualTo('senha_cliente')])
    botao_cadastracliente = SubmitField('Cadastra Cliente')
