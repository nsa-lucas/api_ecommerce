import email
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db
from models import User

users_bp = Blueprint('users',__name__, url_prefix='/api/users')

@users_bp.route('/add', methods=['POST'])

def add_user():
    data = request.json

# VERIFICAR SE USERNAME JA EXISTE - ok
# VERIFICAR SE EMAIL JA EXISTE - ok
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

@users_bp.route('/delete/<int:user_id>', methods=['DELETE'])

def delete_user(user_id):

    user = User.query.get(user_id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    
    return jsonify({'message': 'User not found'}), 404


@users_bp.route('/', methods=['GET'])

def get_all_users():

    users = db.session.query(User).all()

    all_users = []

    for user in users:
        all_users.append({
            'id': user.id,
            'name': user.username,
            'email': user.email
        })

    if all_users:
        return jsonify(all_users)
    
    return jsonify({'message': 'Users not found'}), 404    

@users_bp.route('/update/<int:user_id>', methods=['PUT'])

def update_user(user_id):

    data = request.json

    user = User.query.get(user_id)

    if user:

        if data.get('username'):

            username_already_exists = User.query.filter_by(username=data.get('username')).first()

            if username_already_exists:

                return jsonify({'message': 'Username already exists'}), 404
                
            user.username = data.get('username')
        
        if data.get('email'):

            email_already_exists = User.query.filter_by(email=data['email']).first()

            if email_already_exists:
                
                return jsonify({'message': 'Email already exists'}), 404

            user.email = data.get('email')

        db.session.commit()

        return jsonify({'message': 'User updated successfully'})

    return jsonify({'message': 'User not found'}), 404