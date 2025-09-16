from flask import Blueprint, request, jsonify
from extensions import db
from models import Product

# DEFININDO PREFIXO DE ROTAS PARA PRODUTOS

products_bp = Blueprint('products',__name__, url_prefix='/api/products')

# DEFININDO ROTA DE CADASTRO DE PRODUTOS
@products_bp.route('/add', methods=['POST']) # Rota aceita somente metodo post

def add_product():
    data = request.json

    if data.get('name') and data.get('price'):
        product = Product(
            name=data['name'], 
            price=data['price'], 
            description=data.get('description', '')
        )
        
        db.session.add(product)
        db.session.commit()

        return jsonify({'message': 'Product added successfully'})
    
    return jsonify({'message': 'Invalid Product data'}), 400

# DEFININDO ROTA DE DELEÇÃO DE PRODUTOS
@products_bp.route('/delete/<int:product_id>', methods=['DELETE'])

def delete_product(product_id):
    # Recuperando produto da base de dados
    # Validar se produto existe

    product = Product.query.get(product_id)
    
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})
    
    return jsonify({'message': 'Product not found'}), 404

# DEFININDO ROTA DE LISTAGEM DE PRODUTOS
@products_bp.route('/<int:product_id>', methods=['GET'])

def get_product_detail(product_id):
    product = Product.query.get(product_id)

    if product:
        return jsonify({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description
        })
    
    return jsonify({'message': 'Product not found'}), 404

# DEFININDO ROTA DE LISTAGEM DE TODOS OS PRODUTOS
@products_bp.route('/', methods=['GET'])

def get_all_products():
    products = db.session.query(Product).all()

    all_products = []

    for p in products:
        all_products.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description
        })

    if all_products:
        return jsonify(all_products)
    
    return jsonify({'message': 'Products not found'}), 404

# DEFININDO ROTA DE ATUALIZAÇÃO DE PRODUTO
@products_bp.route('/<int:product_id>', methods=['PUT'])

def update_product(product_id):
    data = request.json

    product = Product.query.get(product_id)

    if product:
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.description = data.get('description', product.description)

        db.session.commit()

        return jsonify({'message': 'Product updated successfully'})

    return jsonify({'message': 'Product not found'}), 404
