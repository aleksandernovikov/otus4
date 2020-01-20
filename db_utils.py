from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from settings import DB_URI

engine = create_engine(DB_URI, pool_pre_ping=True)
Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine),
)


def write_db(*args):
    session = Session()
    for model_instance in args:
        session.add(model_instance)
    session.commit()
