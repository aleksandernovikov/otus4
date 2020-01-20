from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from models import User
from models.base import Base


class Post(Base):
    __tablename__ = 'posts'

    owner_id = Column(Integer, ForeignKey(User.id))

    title = Column(String(100), nullable=False)
    text = Column(Text, nullable=False)
    published = Column(Boolean, default=False)

    author = relationship(User, back_populates='posts', lazy='joined')
    tags = relationship('Tag', secondary='post_tags', back_populates='posts')

    # unique title+owner_id
    __table_args__ = (
        UniqueConstraint('owner_id', 'title', name='title_owner'),
    )
