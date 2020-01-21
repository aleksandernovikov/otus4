from sqlalchemy import Column, Integer, ForeignKey, Table

from models.base import Base


class PostTags(Base):
    __tablename__ = 'post_tags'

    # id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))
