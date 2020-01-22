from sqlalchemy import Column, Integer, ForeignKey

from blog.models.base import Base


class PostTags(Base):
    __tablename__ = 'post_tags'

    id = Column(Integer, primary_key=True)

    post_id = Column(Integer, ForeignKey('posts.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))

    def __repr__(self):
        return f'{__class__} {self.post_id}-{self.tag_id}'
