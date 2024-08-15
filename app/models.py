from app import db, Base
from flask_login import UserMixin
from sqlalchemy import String, Enum, Integer, Column, ForeignKey, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship
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
    __tablename__ = "sneakers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(50), unique=True)
    prize: Mapped[float] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(String(25))

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship('Category', back_populates='sneakers')
    image: Mapped[bytes] = mapped_column(sa.LargeBinary)

    def __repr__(self):
        return f"<Sneaker(name={self.name})>"

class Category(db.Model):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    parent_id = Column(Integer, ForeignKey('categories.id'))

    parent = relationship('Category', remote_side=[id], back_populates='children')
    children = relationship('Category', back_populates='parent')
    sneakers = relationship('Sneaker', back_populates='category')

    def __repr__(self):
        return f"<Category(name={self.name})>"