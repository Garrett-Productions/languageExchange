from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user
from flask import flash
db = "language_exchange"

class Post:
    def __init__(self, db_data ):
        self.id = db_data['id']
        self.user_id= db_data['user_id']
        self.content = db_data['content']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.creator = None

    @staticmethod
    def validate_posts(post):
        is_valid = True 
        if len(post['content']) < 1:
            flash ("Post Content must not be blank", "post")
            is_valid=False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (content, user_id) VALUES (%(content)s, %(user_id)s );"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts JOIN users ON users.id = posts.user_id;"
        all_posts = connectToMySQL(db).query_db(query)
        posts =[]
        for one_post in all_posts:
            each_post = cls(one_post)
            each_post_writer_info = {
                "id": one_post['users.id'],
                "first_name": one_post['first_name'],
                "last_name": one_post['last_name'],
                "email": one_post['email'],
                "password": one_post['password'],
                "social_media": one_post['social_media'],
                "bio": one_post['bio'],
                "goal_content": one_post['goal_content'],
                "created_at": one_post['users.created_at'],
                "updated_at": one_post['users.updated_at']
            }
            writer = user.User(each_post_writer_info)
            each_post.creator = writer
            posts.append(each_post)
        return posts

    @classmethod
    def delete_post(cls,data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)