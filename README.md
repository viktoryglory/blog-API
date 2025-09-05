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
# 1. Create project directory
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