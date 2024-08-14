from app import db
from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
import sqlalchemy as sa

class User(UserMixin, db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(25))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[int] = mapped_column(String(50))

    def __repr__(self):
        return f"User: {self.nickname}"

    def __str__(self):
        return self.nickname.capitalize()


class Sneaker(db.Model):
    __tablename__ = "Sneacker"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(50), unique=True)
    prize: Mapped[float] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(String(25))
    image: Mapped[bytes] = mapped_column(sa.LargeBinary)


    def __repr__(self):
        return f"<Sneacker:{self.name}>"
