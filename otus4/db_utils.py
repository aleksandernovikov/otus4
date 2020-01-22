from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session, sessionmaker

from .settings import DB_URI

engine = create_engine(DB_URI, pool_pre_ping=True)
Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine),
)


def try_commit(current_session):
    try:
        current_session.commit()
    except IntegrityError as e:
        print(e)
        current_session.rollback()
