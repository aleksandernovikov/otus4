from blog.models.base import Base
from otus4.db_utils import engine

if __name__ == '__main__':
    Base.metadata.create_all(engine)
