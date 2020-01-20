from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


class User(Base):
    __tablename__ = 'users'
    username = Column(String(100), nullable=False, unique=True)

    posts = relationship('Post', back_populates='author', lazy='joined')
