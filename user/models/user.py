from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from blog.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)

    posts = relationship('Post', back_populates='author', lazy='joined')

    def __repr__(self):
        return f'{__class__} #{self.id} {self.username}'
