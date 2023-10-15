from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user, user_language_model
from flask import flash
db = "language_exchange"

class User_languages:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.user_id = db_data['user_id']
        self.native_tongue = db_data['native_tongue']
        self.fluent_in = db_data['fluent_in']
        self.learning = db_data['learning']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.creater= None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user_languages (user_id, native_tongue, fluent_in, learning) VALUES (%(user_id)s, %(native_tongue)s, %(fluent_in)s, %(learning)s );"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM user_languages WHERE user_id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        print("-----------results-----------------", results)
        return cls(results[0])

    @classmethod
    def get_all_users_info(cls, data):
        query = "SELECT * FROM user_languages JOIN users ON users.id = user_languages.user_id;"
        all_users_info = connectToMySQL(db).query_db(query, data)
        users_language_info =[]
        for one_user_info in all_users_info:
            each_user = user.User(one_user_info)
            each_user_language_info = {
                "id": one_user_info['users.id'],
                "user_id": one_user_info['user_id'],
                "native_tongue": one_user_info['native_tongue'],
                "fluent_in": one_user_info['fluent_in'],
                "learning": one_user_info['learning'],
                "created_at": one_user_info['users.created_at'],
                "updated_at": one_user_info['users.updated_at']
            }
            writer = user_language_model.User_languages(each_user_language_info)
            each_user.creator = writer
            users_language_info.append(each_user)
        return users_language_info