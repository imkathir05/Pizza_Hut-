## Pizza Hut Django Project

Welcome to the Pizza Hut Django project! This web application allows users to order pizzas online and manage their orders. It's built using Django for the backend, HTML/CSS for the frontend, and MySQL for the database.

## Table of Contents

- [Features]
- [Installation]
- [Usage]
- [Contributing]
- [License]

## Features

- User authentication: Users can register, log in, and log out.
- Pizza menu: Browse and select from a variety of pizzas.
- Online ordering: Add pizzas to the cart and place orders.
- Order history: View and manage past orders.
- Admin dashboard: Manage pizzas, orders, and users (admin credentials required).
- Responsive design: Ensures a seamless experience on various devices.

## Installation
### Prerequisites

- Python 3.x
- MySQL

### Steps

1. Clone the repository:

- git clone https://github.com/imkathir05/pizza-hut-django.git

## Navigate to the project directory:

cd pizza-hut-django

## Create a virtual environment:

python -m venv venv
Activate the virtual environment:

## On Windows:
.\venv\Scripts\activate
## On macOS/Linux:

source venv/bin/activate
Install dependencies:

pip install -r requirements.txt

## Set up the MySQL database:

## Create a MySQL database.
Update the database configuration in pizza_hut/settings.py with your credentials.
Apply migrations:

-python manage.py migrate

## Create a superuser for admin access:

-python manage.py createsuperuser

## Run the development server:

python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.

## Usage
-Create an account or log in.
-Explore the pizza menu and add items to your cart.
-Place an order and view your order history.
-For admin access, log in using the previously created superuser credentials and navigate to http://127.0.0.1:8000/admin/ to manage pizzas, orders, and users.
