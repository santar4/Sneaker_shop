from app import db
from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
import sqlalchemy as sa

# class Sneaker(db.Model):
#     ...
    # id: Mapped[int]
    # name: Mapped[str]
    # descr: Mapped[str]
    # price: Mapped[float]
    # gender: Mapped[str]

    # image: Mapped[bytes] = mapped_column(sa.LargeBinary)
    # image: Mapped[str] = mapped_column(sa.String(255))


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(25))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[int] = mapped_column(String(50))

    is_admin: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f"User: {self.nickname}"

    def __str__(self):
        return self.nickname.capitalize()
