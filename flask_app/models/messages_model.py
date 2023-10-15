from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user #we avoided circular imports by importing the module
from flask import flash
db = "language_exchange"
from datetime import datetime
realdate = '%d-%m-%Y'

class Messages:
    def __init__(self, db_data):
        self.id= db_data['id']
        self.content= db_data['content']
        self.sender_id= db_data['sender_id']
        self.sender= None
        self.receiver_id= db_data['receiver_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @staticmethod
    def validate_messages(message):
        is_valid = True 
        if len(message['content']) < 1:
            flash ("Message must include relevant content", "message")
            is_valid=False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO messages (content, receiver_id, sender_id) VALUES (%(content)s, %(receiver_id)s, %(sender_id)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_messages(cls, data):
        query = """SELECT * FROM messages 
                JOIN users ON sender_id = users.id
                WHERE receiver_id = %(id)s;"""
        messages = []
        results = connectToMySQL(db).query_db(query, data)
        for one_message in results:
            each_message = cls(one_message)
            each_message_writer_info = {
                "id": one_message['users.id'],
                "first_name": one_message['first_name'],
                "last_name": one_message['last_name'],
                "email": one_message['email'],
                "password": one_message['password'],
                "social_media": one_message['social_media'],
                "bio": one_message['bio'],
                "goal_content": one_message['goal_content'],
                "created_at": one_message['users.created_at'],
                "updated_at": one_message['users.updated_at']
            }
            message = user.User(each_message_writer_info)
            each_message.sender = message
            messages.append(each_message)
        return messages

    @classmethod
    def delete_message(cls,data):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)