from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from blog.models.base import Base


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=True)

    posts = relationship(
        'Post',
        secondary='post_tags',
        back_populates='tags'
    )

    def __repr__(self):
        return f'{__class__} #{self.id} {self.title}'
