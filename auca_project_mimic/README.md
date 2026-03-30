# AUCA Project Mimic

A Django-based authentication system that replicates the login functionality for the Adventist University of Central Africa (AUCA) portal. This project provides a clean, responsive login interface with support for both students and staff members, For now only the mimickation of the Login page is implemented.

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- **Clean Login Interface**: A modern, responsive login form with AUCA branding
- **Responsive Design**: Optimized for both desktop and mobile devices
- **User Type Selection**: Support for differentiating between student and staff logins
- **Password Recovery**: "Forgot Password?" functionality link
- **Account Management**: Sign-up link for new users
- **Static Assets Management**: Organized CSS and image storage
- **Django Admin Panel**: Pre-configured Django admin interface
- **Database Ready**: SQLite database setup for development (extensible to production databases)

---

## 📸 Screenshots

### Desktop View
![Desktop Login View](static/img/fulldesk.png)

### Mobile View
![Mobile Login View](static/img/mobileview.png)

---

## 📖 Project Overview

This project is a Django web application that serves as an authentication gateway for AUCA. It's designed to:

1. **Authenticate Users**: Handle login requests for students and staff
2. **Provide a Professional Interface**: Display the AUCA branding with institutional colors
3. **Support Mobile Access**: Responsive design for all device sizes
4. **Be Extensible**: Built with Django to allow easy feature additions

**Current Status**: Development phase with basic login form functionality

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Setup

#### 1. Clone or Download the Project

```bash
cd /path/to/auca_project_mimic
```

#### 2. Create a Virtual Environment

```bash
# On Linux/Mac
python3 -m venv py312-env

# On Windows
python -m venv py312-env
```

#### 3. Activate the Virtual Environment

```bash
# On Linux/Mac
source py312-env/bin/activate

# On Windows
py312-env\Scripts\activate
```

#### 4. Install Dependencies

```bash
pip install django==6.0.3
```

Or if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

#### 5. Apply Database Migrations

```bash
python manage.py migrate
```

#### 6. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

#### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

#### 8. Access the Application

- **Login Page**: Visit `http://127.0.0.1:8000/`
- **Admin Panel**: Visit `http://127.0.0.1:8000/admin/` with your superuser credentials

---

## 📁 Project Structure

```
auca_project_mimic/
├── manage.py                          # Django management script
├── db.sqlite3                         # SQLite database (development)
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies (recommended)
│
├── auca_project_mimic/                # Main project configuration
│   ├── __init__.py
│   ├── settings.py                    # Project settings
│   ├── urls.py                        # Main URL routing
│   ├── asgi.py                        # ASGI configuration
│   ├── wsgi.py                        # WSGI configuration
│   └── __pycache__/
│
├── accounts/                          # Accounts app
│   ├── migrations/                    # Database migrations
│   ├── templates/
│   │   └── accounts/
│   │       └── login.html             # Login page template
│   ├── __pycache__/
│   ├── __init__.py
│   ├── admin.py                       # Admin configuration
│   ├── apps.py                        # App configuration
│   ├── models.py                      # Database models
│   ├── tests.py                       # Unit tests
│   ├── urls.py                        # App URL routing
│   └── views.py                       # View logic
│
└── static/                            # Static files (CSS, JS, Images)
    ├── css/
    │   └── style.css                  # Login page styles
    └── img/
        ├── 10001.png                  # AUCA Logo
        ├── 10002.jpg
        ├── fulldesk.png               # Desktop screenshot
        └── mobileview.png             # Mobile screenshot
```

---

## 💻 Usage

### Basic Login Flow

1. Navigate to `http://127.0.0.1:8000/`
2. Enter your email/ID
3. Enter your password
4. Check "I am a staff" if applicable
5. Click "Sign In"
6. Use "Forgot Password?" to recover your password
7. Click "Sign Up" to create a new account

### Django Admin Panel

1. Go to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Manage users, groups, and other models

### View Raw Login Requests (Development)

The current `views.py` prints login attempts to the console for development purposes:

```bash
# You'll see output like:
# Email: user@example.com
# Password: ****
```

---

## ⚙️ Configuration

### Database Configuration

Edit `auca_project_mimic/settings.py` to change the database:

```python
# Current (SQLite - Development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# For PostgreSQL (Production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'auca_db',
        'USER': 'auca_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files

Collect static files for production:

```bash
python manage.py collectstatic
```

### Security Configuration

Before deploying to production, update these in `settings.py`:

```python
DEBUG = False  # Disable debug mode
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
SECRET_KEY = 'your-secret-key-here'  # Change this!
```

---

## 🤝 Contributing

We welcome contributions from the community! Here's how to add new features or fix bugs:

### Step 1: Fork or Clone the Repository

```bash
git clone https://github.com/yourusername/auca_project_mimic.git
cd auca_project_mimic
```

### Step 2: Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

or for bug fixes:

```bash
git checkout -b bugfix/description-of-bug
```

### Step 3: Make Your Changes

#### Adding a New App

```bash
python manage.py startapp your_app_name
```

Then add it to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'your_app_name',  # Add this
]
```

#### Adding a New View

In your app's `views.py`:

```python
from django.shortcuts import render
from django.http import HttpResponse

def your_view(request):
    # Your view logic here
    return render(request, 'your_template.html')
```

Then register it in your app's `urls.py`:

```python
from django.urls import path
from .views import your_view

urlpatterns = [
    path('your-path/', your_view, name='your_view_name'),
]
```

And include it in the main `urls.py`.

#### Adding a New Model

In your app's `models.py`:

```python
from django.db import models

class YourModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```

Then run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Modifying Styles

Edit `static/css/style.css` directly and refresh your browser.

#### Adding New Templates

Create new templates in `accounts/templates/accounts/` and reference them in your views.

### Step 4: Test Your Changes

```bash
# Run the development server
python manage.py runserver

# Run tests (if any)
python manage.py test
```

### Step 5: Commit Your Changes

```bash
git add .
git commit -m "Feature: Add description of what you added/fixed"
```

Examples:
```bash
git commit -m "Feature: Add password reset functionality"
git commit -m "Fix: Correct login form validation"
git commit -m "Docs: Update README with setup instructions"
```

### Step 6: Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### Step 7: Create a Pull Request

Go to the GitHub repository and create a pull request describing your changes.

### Contribution Guidelines

- **Code Style**: Follow PEP 8 Python style guide
- **Comments**: Add comments to complex logic
- **Testing**: Write tests for new features
- **Documentation**: Update README if needed
- **Commit Messages**: Use descriptive, present-tense messages

---

## 📝 Development Roadmap

Planned features for future versions:

- [ ] User authentication backend implementation
- [ ] Password reset functionality
- [ ] Email verification
- [ ] Dashboard/Home page for authenticated users
- [ ] Student information management
- [ ] Staff management interface
- [ ] Course registration system
- [ ] Grades viewing system
- [ ] Integration with external APIs

---

## 🐛 Troubleshooting

### Common Issues

#### Port 8000 Already in Use

```bash
python manage.py runserver 8001  # Use different port
```

#### Database Error

```bash
# Reset database (careful - deletes all data!)
rm db.sqlite3
python manage.py migrate
```

#### Static Files Not Loading

```bash
python manage.py collectstatic --clear --no-input
```

#### Module Not Found

```bash
# Ensure virtual environment is activated
source py312-env/bin/activate
pip install django==6.0.3
```

---

## 📞 Support

For issues, questions, or suggestions, please:

1. Check the [Troubleshooting](#troubleshooting) section
2. Open an issue on GitHub
3. Contact the project maintainers

---

## 📄 License

This project is open source and available under the MIT License. See the LICENSE file for more information.

---

## 👨‍💼 Project Information

- **Project Name**: AUCA Project Mimic
- **Institution**: Adventist University of Central Africa (AUCA)
- **Framework**: Django 6.0.3
- **Python Version**: 3.8+
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Status**: Active Development

---

## 🙏 Acknowledgments

- Django community for the amazing framework
- AUCA for the inspiration
- All contributors who help improve this project

---

**Last Updated**: March 30, 2026

**Happy Coding!** 🚀
