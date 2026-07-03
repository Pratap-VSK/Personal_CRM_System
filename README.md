# 🚀 Personal CRM System

A lightweight, powerful, and privacy-focused Personal Customer Relationship Management (CRM) system built with Django. This application is designed to help you seamlessly track your network, manage contacts, and log interactions without the clutter of enterprise CRM tools.

This project is part of a broader personal productivity ecosystem (including Task Collaboration, Expense Tracking, and a Digital Journal).

---

## ✨ Key Features
* **Contact Management:** Securely store and categorize personal and professional contacts.
* **Interaction Logging:** Track calls, meetings, and messages to maintain strong relationships.
* **Smart Dashboard:** Get a quick overview of your network and recent interactions.
* **Seamless UI:** Responsive, modern design powered by Bootstrap 5 (Glassmorphism & dark-mode ready elements).
* **Data Privacy:** Strict data isolation ensuring users only access their own records.

---

## 🛠️ Tech Stack
* **Backend:** Django 5 (Python 3.12+)
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Database:** SQLite (Development)
* **Architecture:** Django MTV (Model-Template-View) with Function-Based Views (FBVs)

---

## ⚙️ Complete Step-by-Step Installation & Setup

Follow these exact commands in your terminal to set up the environment and run the application.

### 1. Project Directory Setup
First, make sure you are in your project's root folder:
bash
cd your-project-root-folder

On windows. 
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
On macOS/Linux:
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
Dependencies Installation:
# Upgrade pip to the latest version
python -m pip install --upgrade pip

# Install Django 5
pip install django
pip install -r requirements.txt)
INSTALLED_APPS = [
    # ... Django default apps ...
    'home',
    'accounts',
    'tracker',
    'crm',  # Added for Personal CRM
]
python manage.py makemigrations crm
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
project_root/
│
├── expenses_dashboard/     # Main Django configuration directory
├── crm/                    # Personal CRM Application app folder
│   ├── models.py           # Database architecture (Contact, Interaction)
│   ├── views.py            # Business logic and view controllers
│   ├── forms.py            # ModelForms with custom Bootstrap initialization
│   └── urls.py             # App-specific URL patterns & namespacing
│
├── templates/
│   ├── base.html           # Master layout containing navigation and blocks
│   └── crm/                # CRM specific templates (dashboard, list, detail, form)
│
└── manage.py               # Django administrative script

**Intern ID: CITS3073
**
