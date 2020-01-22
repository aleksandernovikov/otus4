import os
import json
from random import sample

from sqlalchemy.exc import IntegrityError

from otus4.db_utils import Session, try_commit
from blog.models import Post, Tag
from user.models import User

session = Session()


def fill():
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


def load_data(filename):
    """
    Загрузка данных из файла с json данными
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(dir_path, filename)

    with open(full_path) as f:
        return json.load(f)


def get_or_create(model, **kwargs):
    object = model(**kwargs)
    session.add(object)
    try:
        session.flush()
        session.commit()
    except IntegrityError:
        session.rollback()
        object = session.query(model).filter_by(**kwargs).one()
    return object


if __name__ == '__main__':

    data = load_data('fixtures/data.json')
    posts = data.get('posts')

    for post in posts:
        user_data = post.get('owner')
        user = get_or_create(User, **user_data)
        print(user_data, user)

        tags = [get_or_create(Tag, **tag_data) for tag_data in post.get('tags')]
        print(tags)

        post = get_or_create(Post, owner_id=user.id, title=post.get('title'), text=post.get('text'), tags=tags)
        print(post)
