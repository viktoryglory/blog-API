from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.models import User

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Validasi input
        if not data or not data.get('username') or not data.get('email') or not data.get('password'):
            return jsonify({'message': 'Username, email, and password are required'}), 400
        
        # Cek jika user sudah ada
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'message': 'Username already exists'}), 409
        
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'Email already exists'}), 409
        
        # Buat user baru
        user = User(
            username=data['username'],
            email=data['email']
        )
        user.set_password(data['password'])
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            'message': 'User created successfully',
            'user': user.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        # Validasi input
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({'message': 'Username and password are required'}), 400
        
        # Cari user
        user = User.query.filter_by(username=data['username']).first()
        
        # Verifikasi password
        if user and user.check_password(data['password']):
            # Pastikan identity adalah string
            access_token = create_access_token(identity=str(user.id))
            return jsonify({
                'message': 'Login successful',
                'access_token': access_token,
                'user': user.to_dict()
            }), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401
            
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    try:
        user_id = get_jwt_identity()
        # Convert string back to integer untuk query
        user = User.query.get(int(user_id))
        
        if not user:
            return jsonify({'message': 'User not found'}), 404
        
        return jsonify({'user': user.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500