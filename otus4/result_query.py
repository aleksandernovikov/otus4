from sqlalchemy import func

from otus4.db_utils import Session
from blog.models import Post, PostTags
from user.models import User

if __name__ == '__main__':
    """
    Выбрать все посты конкретного пользователя с 2-мя любыми тегами. 
    """
    session = Session()
    username = 'Анна'
    tags_count = 2

    posts = session.query(
        Post
    ).join(
        PostTags
    ).filter(
        User.username == username,
    ).having(
        func.count(PostTags.tag_id) == tags_count
    ).group_by(
        Post.id
    ).all()
    """
    SELECT posts.id AS posts_id, 
           posts.owner_id AS posts_owner_id, 
           posts.title AS posts_title, 
           posts.text AS posts_text
    FROM users,
         posts
             JOIN post_tags ON posts.id = post_tags.post_id
    WHERE users.username = ?
    GROUP BY posts.id
    HAVING count(post_tags.tag_id) = ?
    """
    print(posts)
