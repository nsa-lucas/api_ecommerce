from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db
from models import User

users_bp = Blueprint('users',__name__, url_prefix='/api/users')

@users_bp.route('/add', methods=['POST'])

def add_user():
    data = request.json

# VERIFICAR SE USERNAME JA EXISTE - pendente
# VERIFICAR SE EMAIL JA EXISTE - pendente
# CRIPTOGRAFAR SENHA ANTES IR PRA BANCO DE DADOS - ok

    

    hashed_password = generate_password_hash(data['password'])

    # if username_already_exists or email_already_exists:
        

    if data.get('username') and data.get('email') and data.get('password'):

        username_already_exists = User.query.filter_by(username=data['username']).first()
        email_already_exists = User.query.filter_by(email=data['email']).first()


        if not username_already_exists and not email_already_exists:
            user = User(
                username = data['username'],
                email = data['email'],
                password = hashed_password
            )

            db.session.add(user)
            db.session.commit()

            return jsonify({
                'message':'User added successfully'
            })

        return jsonify({
                'message':'Email or username already exists'
        }),400

    return jsonify({
        'message':'Invalid user data'
    }),400

   

    

    