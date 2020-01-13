# from sqlalchemy import Column, Integer, String, Boolean, Text
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
#
# class Post(Base):
#     __tablename__ = 'posts'
#
#     id = Column(Integer, primary_key=True)
#     owner = Column(Integer, nullable=False)
#     title = Column(String(100), nullable=False)
#     text = Column(Text, nullable=False)
#     published = Column(Boolean, default=False)
