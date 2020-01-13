from models import User, Post
from settings import Session

session = Session()


def write_db(*args):
    for model_instance in args:
        session.add(model_instance)
    session.commit()


def q(model):
    return session.query(model)


if __name__ == '__main__':
    # author = User(username='Ivan')

    # session.add(author)
    # session.flush()

    # write_db(author)
    #
    # write_db(
    #     Post(owner=author.id, title='first', text='First text'),
    #     Post(owner=author.id, title='second', text='Second text'),
    # )

    p = session.query(Post)
    print(list(p))
    print(p.all())

    f = p.first()
    print(f)

    print(f.owner)
    print(f.owner.username)
