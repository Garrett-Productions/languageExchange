from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.user_language_model import User_languages
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from datetime import datetime
realdate = '%d-%m-%Y'


@app.route('/createProfile', methods=['POST'])
def createProfile():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "user_id": session['user_id'],
        "native_tongue": request.form['native_tongue'],
        "fluent_in": request.form['fluent_in'],
        "learning": request.form['learning']
    }
    User_languages.save(data)
    return redirect('/dashboard')


@app.route('/dashboard')
def profilePage():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id'],
    }
    return render_template("dashboard.html", user=User.get_by_id(data), languages = User_languages.get_all(data))