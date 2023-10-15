import re
from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.user_language_model import User_languages
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from datetime import datetime
realdate = '%d-%m-%Y'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods = ['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data) 
    session['user_id'] = id
    return redirect('/setup')


@app.route('/setup')
def setup():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id'],
    }
    return render_template("setup.html", user=User.get_by_id(data))

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid email", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("invalid Password", "login")
        return redirect ('/')
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    return redirect('/dashboard')

@app.route('/about_me', methods= ['POST'])
def about_me():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id'],
        "social_media": request.form['social_media'],
        "bio": request.form['bio']
    }
    User.save_bio(data)
    return redirect('/dashboard')


@app.route('/about_my_goals', methods= ['POST'])
def about_my_goals():
    if 'user_id' not in session:
        return redirect('/logout')
    print(request.form['goal_content'])
    data = {
        "id": session['user_id'],
        "goal_content": request.form['goal_content']
    }
    User.save_goals(data)
    return redirect('/dashboard')



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')