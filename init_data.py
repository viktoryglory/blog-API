from app import create_app, db
from app.models import User, Category

def init_data():
    app = create_app()
    
    with app.app_context():
        # Hapus dan buat ulang tabel
        db.drop_all()
        db.create_all()
        
        # Buat user admin
        admin_user = User(
            username='admin',
            email='admin@blog.com',
            is_admin=True
        )
        admin_user.set_password('admin123')
        
        # Buat user regular
        regular_user = User(
            username='user',
            email='user@blog.com',
            is_admin=False
        )
        regular_user.set_password('user123')
        
        db.session.add(admin_user)
        db.session.add(regular_user)
        
        # Buat kategori default
        categories = [
            Category(name='Technology', description='Posts about technology and programming'),
            Category(name='Lifestyle', description='Posts about lifestyle and personal development'),
            Category(name='Travel', description='Posts about travel and adventures')
        ]
        
        for category in categories:
            db.session.add(category)
        
        db.session.commit()
        print("Database initialized successfully!")
        print("Admin user: username=admin, password=admin123")
        print("Regular user: username=user, password=user123")

if __name__ == '__main__':
    init_data()