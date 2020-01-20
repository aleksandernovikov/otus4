from sqlalchemy import Column, Integer, ForeignKey, Table

from models.base import Base


class PostTags(Base):
    __tablename__ = 'post_tags'

    # id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))

# posts_tags = Table(
#     'posts_tags',
#     Base.metadata,
#     Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
#     Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
# )
