from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)

    posts = relationship('Post', back_populates='author')

    def __repr__(self):
        return f'{__class__} #{self.id}, {self.username}'


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    owner = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(100), nullable=False)
    text = Column(Text, nullable=False)
    published = Column(Boolean, default=False)

    author = relationship(User, back_populates='posts')

    # tags = relationship('')
    def __repr__(self):
        return f'{__class__} #{self.id}, {self.title}'

# class Tag(Base):
#     __tablename__ = 'tags'
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(100), nullable=False)
#
#     posts = relationship(Post, secondary='PostsTags', back_populates='tags')
#
#
# class PostsTags(Base):
#     __tablename__ = 'posts_tags'
#     id = Column(Integer, primary_key=True)
#     post_id = Column(Integer, ForeignKey(Post.id), nullable=False)
#     tag_id = Column(Integer, ForeignKey(Tag.id), nullable=False)
