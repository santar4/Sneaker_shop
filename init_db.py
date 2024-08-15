import os

from app import app, db
from app.models import User, Sneaker, Category
from werkzeug.security import generate_password_hash, check_password_hash


def create_mock_data():

    category1 = Category(name='Демісезон')


        # Додайте кожен об'єкт окремо
    db.session.add(category1)


    db.session.commit()

    print("mock data added")




with app.app_context():
    db.create_all()
    print("Create database")
    create_mock_data()

