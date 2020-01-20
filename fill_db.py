from random import sample

from sqlalchemy.exc import IntegrityError

from db_utils import Session
from models import User, Post, Tag

session = Session()


def try_commit(current_session):
    try:
        current_session.commit()
    except IntegrityError as e:
        print(e)
        current_session.rollback()


if __name__ == '__main__':
    """
    Наполнение БД
    """
    for user_id in range(1, 3):
        user = User(username=f'User#{user_id}')
        session.add(user)
    try_commit(session)

    users = session.query(User).all()
    for user in users:
        for post in range(1, 4):
            p = Post(owner_id=user.id, title=f'Post #{post} by user {user.username}', text=f'Some text ')
            session.add(p)
        try_commit(session)

    for tag_id in range(1, 10):
        tag = Tag(title=f'Tag{tag_id}')
        session.add(tag)
    try_commit(session)

    all_posts = session.query(Post).all()
    all_tags = session.query(Tag).all()

    for post in all_posts:
        random_tags = sample(all_tags, post.id)
        post.tags.extend(random_tags)
    try_commit(session)
