from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Post, Category, Comment, User
from app.utils import admin_required

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({'message': 'Blog API is running!'})

@bp.route('/posts', methods=['GET'])
def get_posts():
    try:
        posts = Post.query.all()
        return jsonify({
            'posts': [post.to_dict() for post in posts]
        }), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        return jsonify({'post': post.to_dict()}), 200
    except Exception as e:
        return jsonify({'message': 'Post not found'}), 404

@bp.route('/categories', methods=['GET'])
def get_categories():
    try:
        categories = Category.query.all()
        return jsonify({
            'categories': [category.to_dict() for category in categories]
        }), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    try:
        data = request.get_json()
        user_id = get_jwt_identity()
        # Convert string to integer
        user_id_int = int(user_id)
        
        # Validasi input
        if not data or not data.get('title') or not data.get('content') or not data.get('category_id'):
            return jsonify({'message': 'Title, content, and category_id are required'}), 400
        
        # Cek apakah kategori exists
        category = Category.query.get(data['category_id'])
        if not category:
            return jsonify({'message': 'Category not found'}), 404
        
        # Buat post baru
        post = Post(
            title=data['title'],
            content=data['content'],
            user_id=user_id_int,
            category_id=data['category_id']
        )
        
        db.session.add(post)
        db.session.commit()
        
        return jsonify({
            'message': 'Post created successfully',
            'post': post.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/posts/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    try:
        data = request.get_json()
        user_id = get_jwt_identity()
        user_id_int = int(user_id)
        
        post = Post.query.get_or_404(post_id)
        user = User.query.get(user_id_int)
        
        # Cek authorization (hanya author atau admin yang bisa edit)
        if post.user_id != user_id_int and not user.is_admin:
            return jsonify({'message': 'Unauthorized'}), 403
        
        # Update fields
        if 'title' in data:
            post.title = data['title']
        if 'content' in data:
            post.content = data['content']
        if 'category_id' in data:
            category = Category.query.get(data['category_id'])
            if not category:
                return jsonify({'message': 'Category not found'}), 404
            post.category_id = data['category_id']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Post updated successfully',
            'post': post.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/posts/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    try:
        user_id = get_jwt_identity()
        user_id_int = int(user_id)
        
        post = Post.query.get_or_404(post_id)
        user = User.query.get(user_id_int)
        
        # Cek authorization (hanya author atau admin yang bisa delete)
        if post.user_id != user_id_int and not user.is_admin:
            return jsonify({'message': 'Unauthorized'}), 403
        
        db.session.delete(post)
        db.session.commit()
        
        return jsonify({'message': 'Post deleted successfully'}), 200
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/posts/<int:post_id>/comments', methods=['GET'])
def get_post_comments(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
        
        return jsonify({
            'post_id': post_id,
            'comments': [comment.to_dict() for comment in comments]
        }), 200
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/posts/<int:post_id>/comments', methods=['POST'])
@jwt_required()
def create_comment(post_id):
    try:
        data = request.get_json()
        user_id = get_jwt_identity()
        user_id_int = int(user_id)
        
        # Validasi post exists
        post = Post.query.get_or_404(post_id)
        
        # Validasi input
        if not data or not data.get('content'):
            return jsonify({'message': 'Content is required'}), 400
        
        # Buat comment baru
        comment = Comment(
            content=data['content'],
            user_id=user_id_int,
            post_id=post_id
        )
        
        db.session.add(comment)
        db.session.commit()
        
        return jsonify({
            'message': 'Comment created successfully',
            'comment': comment.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/comments/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(comment_id):
    try:
        user_id = get_jwt_identity()
        user_id_int = int(user_id)
        
        comment = Comment.query.get_or_404(comment_id)
        user = User.query.get(user_id_int)
        
        # Cek authorization (hanya author atau admin yang bisa delete)
        if comment.user_id != user_id_int and not user.is_admin:
            return jsonify({'message': 'Unauthorized'}), 403
        
        db.session.delete(comment)
        db.session.commit()
        
        return jsonify({'message': 'Comment deleted successfully'}), 200
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/categories', methods=['POST'])
@jwt_required()
@admin_required
def create_category():
    try:
        data = request.get_json()
        
        # Validasi input
        if not data or not data.get('name'):
            return jsonify({'message': 'Name is required'}), 400
        
        # Cek jika kategori sudah ada
        if Category.query.filter_by(name=data['name']).first():
            return jsonify({'message': 'Category already exists'}), 409
        
        # Buat kategori baru
        category = Category(
            name=data['name'],
            description=data.get('description', '')
        )
        
        db.session.add(category)
        db.session.commit()
        
        return jsonify({
            'message': 'Category created successfully',
            'category': category.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/categories/<int:category_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_category(category_id):
    try:
        data = request.get_json()
        
        category = Category.query.get_or_404(category_id)
        
        # Update fields
        if 'name' in data:
            # Cek jika nama baru sudah digunakan oleh kategori lain
            existing_category = Category.query.filter_by(name=data['name']).first()
            if existing_category and existing_category.id != category_id:
                return jsonify({'message': 'Category name already exists'}), 409
            category.name = data['name']
            
        if 'description' in data:
            category.description = data['description']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Category updated successfully',
            'category': category.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@bp.route('/categories/<int:category_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_category(category_id):
    try:
        category = Category.query.get_or_404(category_id)
        
        # Cek jika kategori memiliki posts
        if category.posts.count() > 0:
            return jsonify({'message': 'Cannot delete category with posts'}), 400
        
        db.session.delete(category)
        db.session.commit()
        
        return jsonify({'message': 'Category deleted successfully'}), 200
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500