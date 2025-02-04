# Little Lemon Restaurant API

This is the backend API project for the Little Lemon Restaurant, developed as part of the Meta Backend Developer Capstone course. The API provides functionality for menu management and table booking operations.

## 🚀 Features

- Menu Items Management
- Table Booking System
- User Authentication
- API Token Authentication

## 🛠️ Technologies Used

- Django 5.1.5
- Django REST Framework 3.15.2
- Djoser 2.3.1

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/v0id-user/littlelemon-backend-capstone-meta.git
   cd littlelemon-backend-capstone-meta
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## 🔌 API Endpoints

### Menu Endpoints
- `GET /api/menu/` - List all menu items
- `GET /api/menu/<int:pk>/` - Retrieve a specific menu item
- `POST /api/menu/` - Create a new menu item (auth required)
- `PUT /api/menu/<int:pk>/` - Update a menu item (auth required)
- `DELETE /api/menu/<int:pk>/` - Delete a menu item (auth required)

### Booking Endpoints
- `GET /api/bookings/` - List all bookings (auth required)
- `POST /api/bookings/` - Create a new booking (auth required)

### Authentication Endpoints
- `POST /api/api-token-auth/` - Obtain authentication token
- Additional auth endpoints provided by Djoser

## 🔐 Authentication

The API uses token-based authentication. To access protected endpoints:
1. Obtain a token from `/api/api-token-auth/`
2. Include the token in the request header:
   ```
   Authorization: Token <your-token>
   ```

## 📝 Models

### Menu
- `item`: CharField (max_length=100)
- `price`: IntegerField

### Booking
- `tableno`: IntegerField
- `persons`: IntegerField

## 👥 Contributing

This project is part of the Meta Backend Developer Certification. While it's primarily for educational purposes, feedback and suggestions are welcome.

## 📄 License

This project is part of the Meta Backend Developer Certification coursework.

## 🔗 Links

- [GitHub Repository](https://github.com/v0id-user/littlelemon-backend-capstone-meta/)
