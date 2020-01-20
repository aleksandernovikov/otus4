from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base


class ReprMixin:
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        manager = self._sa_class_manager
        return f'{manager.class_} #{self.id}'


Base = declarative_base(cls=ReprMixin)
