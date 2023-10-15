from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.post import Post
from flask_app.models.user import User
from flask_app.models.user_language_model import User_languages
from datetime import datetime
realdate = '%d-%m-%Y'

@app.route('/community')
def show_users():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template("community.html", user=User.get_by_id(data), all_users_info = User_languages.get_all_users_info(data))