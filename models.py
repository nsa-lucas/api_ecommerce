from extensions import db

# Produto (id, name, price, description)
class Product(db.Model):
    # Definindo colunas da tabela produto
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
