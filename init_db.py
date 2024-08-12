import os

from app import app, db
from app.models import User, Sneaker
from werkzeug.security import generate_password_hash, check_password_hash


def create_mock_data():
    file_path = os.path.abspath("static/media/cholovichi-krosivky-nike-sb-dunk-low-green-lobster-86777256136882.jpg")

    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            photo_data = file.read()
    else:
        print(f"Файл не знайдено: {file_path}")
        photo_data = None

    if photo_data is not None:
        ab = Sneaker(
            name="New Balance 1906",
            description="Upper Textile: a very light material, which is offered in various colors and is used primarily for the production of summer shoes. Synthetics: unlike textiles, synthetic fibers are stronger, more durable and dry faster.",
            prize="6 100 грн",
            gender="male",
            image=photo_data
        )

        # Переконайтесь, що всі поля не є None
        if all([ab.name, ab.description, ab.prize, ab.gender, ab.image]):
            db.session.add_all([ab])

        else:
            print("Дані для створення об'єкта 'Sneaker' неповні.")
    else:
        print("Не вдалося завантажити фото, об'єкт 'Sneaker' не буде створений.")

    db.session.commit()
    print("mock data added")




with app.app_context():
    # db.create_all()
    print("Create database")
    create_mock_data()
