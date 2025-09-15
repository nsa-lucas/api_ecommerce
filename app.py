from flask import Flask, request

# IMPORTANDO BANCO DE DADOS SQLALCHEMY- SALVA OS DADOS EM UM ARQUIVO TXT 
# USADO EM APLICACOES MAIS SIMPLES OU EM MODO DEV
from flask_sqlalchemy import SQLAlchemy 

# CRIANDO INSTANCIA DO FLASK
app = Flask(__name__) 

# DEFININDO CAMINHO DO BANCO DE DADOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# MODELANDO BANCO DE DADOS

# Produto (id, name, price, description)
class Product(db.Model):
    # Definindo colunas da tabela produto
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


with app.app_context():
    db.create_all()


# DEFININDO ROTA DE CADASTRO DE PRODUTOS
@app.route('/api/products/add', methods=['POST']) # Rota aceita somente metodo post

def add_product():
    data = request.json
    product = Product(name=data['name'], price=data['price'], description=data.get('description', ''))
    db.session.add(product)
    db.session.commit()

    return 'Produto cadastrado com sucesso !'

# DEFININDO ROTA RAIZ E FUNCAO QUE SERA EXECUTADA AO REQUISITAR
@app.route('/')

def hello_world():
    return 'Hello World'

# ativando modo debug - sempre em modo dev

if __name__ == "__main__":
    app.run(debug=True)
    