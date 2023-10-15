from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.post import Post
from flask_app.models.user import User
from flask_app.models.user_language_model import User_languages
from datetime import datetime
realdate = '%d-%m-%Y'


@app.route('/post_message', methods = ['POST'])
def post_message():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Post.validate_posts(request.form):
        return redirect('/dashboard')
    data = {
        'user_id': session['user_id'],
        'content': request.form['content']
    }
    print("-------aaa-------", data)
    Post.save(data)
    return redirect('/allPosts') 
#redirect to a different route that renders the same page, maybe a get all posts
#this next route will have the post.get_all passed through when rednering the template

@app.route('/allPosts')
def show_posts():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template("allPosts.html", user=User.get_by_id(data), all_posts= Post.get_all(), dtformat=realdate)



@app.route ('/delete_post/<int:id>')
def delete_post(id):
    data = {
        'id': id
    }
    Post.delete_post(data)
    return redirect('/dashboard')
