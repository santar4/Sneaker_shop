from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash


def create_mock_data():
    u = User(nickname="admin_vaivinc", email="admin_vaivinc@ex.com", password=generate_password_hash("admin_vaivinc"))
    e = User(nickname="admin_devasted", email="admin_devasted@ex.com", password=generate_password_hash("admin_devasted"))

    db.session.add_all([u, e])
    db.session.commit()

    print("Data created")


with app.app_context():
    db.create_all()
    print("Create database")
    create_mock_data()


