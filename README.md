# Library Management System

A modern web-based library management system built with Django, featuring user authentication, book management, borrowing system, and wishlists.

## Features

- User Registration and Authentication
- Book Catalog with Search
- Book Details with Cover Images
- Book Borrowing System
- Personal Wishlist
- Responsive Design
- Admin Interface

## Requirements

- Python 3.8+
- Django 5.2.1
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd library-system
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Usage

1. Register a new account or login with existing credentials
2. Browse the book collection
3. View book details
4. Borrow books and manage your borrowed books
5. Add books to your wishlist
6. Return books when finished

## Admin Interface

Access the admin interface at http://127.0.0.1:8000/admin to:
- Manage books
- Manage users
- View and manage borrowed books
- View wishlists

## License

This project is licensed under the MIT License - see the LICENSE file for details. 