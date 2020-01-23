from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from blog.models.base import Base
from user.models import User


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)

    owner_id = Column(Integer, ForeignKey(User.id))

    title = Column(String(100), nullable=False)
    text = Column(Text, nullable=False)

    author = relationship(User, back_populates='posts')
    tags = relationship('Tag', secondary='post_tags', back_populates='posts')

    # unique title+owner_id
    __table_args__ = (
        UniqueConstraint('owner_id', 'title', name='title_owner'),
    )

    def __repr__(self):
        return f'{__class__}  #{self.id} {self.title}'
