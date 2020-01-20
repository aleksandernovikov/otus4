from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base import Base


class Tag(Base):
    __tablename__ = 'tags'

    title = Column(String(100), nullable=False, unique=True)

    posts = relationship(
        'Post',
        secondary='post_tags',
        back_populates='tags'
    )
