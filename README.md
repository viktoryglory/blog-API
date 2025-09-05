# 🚀 Blog API - Flask RESTful Backend

<div align="center">

![Flask](https://img.shields.io/badge/Flask-2.3.3-important?style=for-the-badge&logo=flask)
![JWT](https://img.shields.io/badge/JWT-Authentication-yellow?style=for-the-badge&logo=json-web-tokens)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&logo=python)
![RESTful](https://img.shields.io/badge/RESTful-API-success?style=for-the-badge&logo=api)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)

**A powerful and secure backend API for blogging platform built with Flask and JWT authentication**

</div>

## 📖 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#-tech-stack)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [⚙️ Configuration](#-configuration)
- [🔐 API Endpoints](#-api-endpoints)
- [🎯 Usage Examples](#-usage-examples)
- [🧪 Testing](#-testing)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## ✨ Features

- **🔐 JWT Authentication** - Secure login/register system
- **📝 Post Management** - Full CRUD operations for blog posts
- **🏷️ Category System** - Organized content categorization
- **💬 Comment System** - User engagement with comments
- **👑 Role-Based Access** - Admin vs User permissions
- **🛡️ Input Validation** - Comprehensive data validation
- **📊 Pagination Ready** - Scalable API structure
- **🔒 Security** - Password hashing with bcrypt

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Flask** | 2.3.3 | Web framework |
| **SQLAlchemy** | 3.0.5 | ORM for database |
| **Flask-JWT-Extended** | 4.5.3 | JWT authentication |
| **Flask-Migrate** | 4.0.5 | Database migrations |
| **bcrypt** | 4.0.1 | Password hashing |
| **Python** | 3.8+ | Programming language |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool

### One-Command Setup

```bash
# Clone and setup (if using git)
git clone <your-repo-url>
cd blog-api

# Create virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_data.py

# Run the application
python run.py

```

Your API will be running at http://localhost:5000 🎉

## 📦 Installation

### Step-by-Step Guide
## 1. Create project directory
```bash
mkdir blog-api
cd blog-api
```

### 2. Set up virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies
```bash
pip install flask==2.3.3 flask-sqlalchemy==3.0.5 flask-migrate==4.0.5
pip install flask-jwt-extended==4.5.3 flask-cors==4.0.0
pip install bcrypt==4.0.1 python-dotenv==1.0.0
```

## 4. Or use requirements.txt
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration
## Environment Variables

Create a .env file in the root directory:
```bash
# Database Configuration
DATABASE_URL=sqlite:///app.db

# JWT Configuration
SECRET_KEY=your-super-secret-key-change-in-production
JWT_SECRET_KEY=your-jwt-secret-key-change-in-production

# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
```

## Project Structure
```text
blog-api/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── auth.py              # Authentication routes
│   ├── models.py            # Database models
│   ├── routes.py            # Main API routes
│   └── utils.py             # Utility functions
├── migrations/              # Database migrations
├── tests/                   # Test files
├── .env                     # Environment variables
├── config.py                # Configuration settings
├── init_data.py             # Database initialization
├── requirements.txt         # Dependencies
└── run.py                   # Application entry point
```

# 🔐 API Endpoints

## Authentication Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | /posts | Get all posts | ❌ |
| GET | /posts/<id> | Get single post | ❌ |
| POST | /posts | Create new post | ✅ |
| PUT | /posts/<id> | Update post | ✅ (User/Admin) |
| DELETE | /posts/<id> | Delete post | ✅ (User/Admin) |

## Comments Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | /posts/<id>/comments | Get post comments | ❌ |
| POST | /posts/<id>/comments | Create comment | ✅ |
| DELETE | /comments/<id> | Delete comment | ✅ (User/Admin) |

## Categories Endpoints (Admin Only)
## Comments Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | /categories | Get all categories | ❌ |
| POST | /categories | Create category | ✅ (Admin) |
| PUT | /categories/<id> | Update category | ✅ (Admin) |
| DELETE | //categories/<id> | Delete category | ✅ (Admin) |

## 🎯 Usage Examples

## 🔐 Authentication

**Register a new user:**
```bash
curl -X POST http://localhost:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "password123"
  }'
  ```

**Login and get JWT token:**
```bash
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'
```

## 📝 Posts Operations

**Create a new post:**
```bash
curl -X POST http://localhost:5000/posts \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my first post",
    "category_id": 1
  }'
```

**Get all posts:**
```bash
curl http://localhost:5000/posts
```

## 💬 Comments Operations
**Add a comment to post:**
```bash
curl -X POST http://localhost:5000/posts/1/comments \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "content": "Great post! Very informative."
  }'
```

## 🏷️ Category Operations (Admin Only)
**Create a new category:**
```bash
curl -X POST http://localhost:5000/categories \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ADMIN_JWT_TOKEN" \
  -d '{
    "name": "Technology",
    "description": "Posts about technology and programming"
  }'
```

## 🧪 Testing
**Run Tests**
```bash
python -m unittest discover tests
```

**Test with curl Examples**
Test authentication:
```bash
# Test login
curl -X POST -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}' \
  http://localhost:5000/auth/login

# Test protected endpoint
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:5000/auth/profile
```

Test posts API:
```bash
# Get all posts
curl http://localhost:5000/posts

# Create a post
curl -X POST -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"title":"Test","content":"Test content","category_id":1}' \
  http://localhost:5000/posts
```

## 🤝 Contributing
We welcome contributions! Please follow these steps:

1. Fork the project
2. Create a feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## Development Setup
```bash
# 1. Fork and clone the repository
git clone https://github.com/your-username/blog-api.git
cd blog-api

# 2. Set up development environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# 3. Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov  # for testing

# 4. Run tests
python -m pytest tests/ -v

# 5. Make your changes and test
```

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support
If you have any questions or need help:

1. Check the API Documentation
2. Look at existing Issues
3. Create a new Issue
4. Email: feriyasin01@gmail.com

<div align="center">
⭐ Don't forget to star this repository if you find it useful!

https://api.star-history.com/svg?repos=your-username/blog-api&type=Date

</div>

## 🙏 Acknowledgments
+ Flask community for the excellent framework
+ JWT team for authentication solution
+ SQLAlchemy for ORM capabilities
+ All contributors who helped improve this project