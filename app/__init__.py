from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    # JWT configuration - PASTIKAN untuk menghindari circular imports
    from app.models import User
    
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        # Pastikan identity adalah string
        return str(user.id) if hasattr(user, 'id') else str(user)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        # Convert string back to integer untuk query
        return User.query.get(int(identity))

    @jwt.additional_claims_loader
    def add_claims_to_access_token(identity):
        user = User.query.get(int(identity))
        return {"is_admin": user.is_admin} if user else {"is_admin": False}

    # Register blueprints
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app