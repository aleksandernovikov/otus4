from sqlalchemy import func

from db_utils import Session
from models import Post, User, Tag, PostTags

if __name__ == '__main__':
    """
    Выбрать все посты конкретного пользователя с 2-мя любыми тегами. 
    """
    session = Session()
    username = 'User#1'
    posts = session.query(Post).join(User).join(PostTags).filter(User.username == username).count()
    print(posts)
    # for post in posts:
    #     print(post.tags)
