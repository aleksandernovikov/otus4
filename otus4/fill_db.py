import os
import json

from sqlalchemy.orm.exc import NoResultFound

from otus4.db_utils import Session
from blog.models import Post, Tag
from user.models import User

session = Session()


def load_data(filename):
    """
    Загрузка данных из файла с json данными
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(dir_path, filename)

    with open(full_path) as f:
        return json.load(f)


def get_or_create(model, **kwargs):
    """
    Получить запись или создать, если ее нет
    """
    object_default_data = {}
    if 'default' in kwargs:
        object_default_data = kwargs.pop('default')
    try:
        object = session.query(model).filter_by(**kwargs).one()
    except NoResultFound:
        object = model(**kwargs, **object_default_data)
        session.add(object)
        session.flush()
        session.commit()
    return object


if __name__ == '__main__':
    """
    Наполнение базы данными
    """
    data = load_data('fixtures/data.json')
    posts = data.get('posts')

    for post in posts:
        user_data = post.get('owner')
        user = get_or_create(User, **user_data)

        tags = [get_or_create(Tag, **tag_data) for tag_data in post.get('tags')]

        get_or_create(
            Post,
            owner_id=user.id,
            title=post.get('title'),
            text=post.get('text'),
            default={'tags': tags}
        )
