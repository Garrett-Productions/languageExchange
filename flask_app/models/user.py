from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user_language_model
import re    
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
password_regex = re.compile(r'^(?=.[a-z])(?=.[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
db = "language_exchange"

class User:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.social_media = db_data['social_media']
        self.bio = db_data['bio']
        self.goal_content = db_data['goal_content']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.posts=[]


    @staticmethod
    def validate_register(user):
        is_valid = True 
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query,user)
        print(results), "--------------------"
        if len(results) >= 1:
            flash ("Email is already in use", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email.", "register")
            is_valid= False
        if len(user['first_name']) < 2:
            flash ("First name must be at least 3 characters", "register")
            is_valid=False
        if len(user['last_name']) < 2:
            flash ("Last name must be at least 3 characters", "register")
            is_valid=False
        if len(user['password']) < 8:
            flash ("Password must be at least 8 characters", "register")
            is_valid=False
        if user['password'] != user['confirm']:
            flash ("Passwords Do Not Match", "register")
            is_valid=False
        return is_valid


    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        print("here are my results", results)
        return results[0]

    @classmethod 
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        language_exchange = connectToMySQL(db).query_db(query)
        users =[]
        for users in language_exchange:
            users.append(cls(users))
        return users

    @classmethod
    def save_bio(cls, data):
        query = "UPDATE users SET social_media=%(social_media)s, bio=%(bio)s WHERE id=%(id)s;"
        return connectToMySQL(db).query_db(query,data)


    @classmethod
    def save_goals(cls, data):
        query = "UPDATE users SET goal_content=%(goal_content)s WHERE id=%(id)s;"
        return connectToMySQL(db).query_db(query,data)