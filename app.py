from flask import Flask

from extensions import db
from routes import register_routes


# CRIANDO INSTANCIA DO FLASK
app = Flask(__name__) 

# DEFININDO CAMINHO DO BANCO DE DADOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db.init_app(app)

with app.app_context():
    db.create_all()

register_routes(app)

# DEFININDO ROTA RAIZ E FUNCAO QUE SERA EXECUTADA AO REQUISITAR
@app.route('/')

def hello_world():
    return 'Hello World'

# ativando modo debug - sempre em modo dev
if __name__ == "__main__":
    app.run(debug=True)
    