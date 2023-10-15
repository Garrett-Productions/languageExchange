from email import message
from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.post import Post
from flask_app.models.user import User
from flask_app.models.user_language_model import User_languages
from flask_app.models.messages_model import Messages
from datetime import datetime
realdate = '%d-%m-%Y'


@app.route('/sendMessage/<int:receiver_id>')
def sendMessage(receiver_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": receiver_id
    }
    print("check right here")
    print(session['user_id'])
    return render_template("messages.html", receiver=User.get_by_id(data))


@app.route('/createMessage', methods=['POST'])
def createMessage():
    if 'user_id' not in session:
        return redirect('/logout') 
    if not Messages.validate_messages(request.form):
        return redirect('/myMessages')
    data = {
        "content": request.form['content'],
        "sender_id": session['user_id'],
        "receiver_id": request.form['receiver_id']
    }
    Messages.save(data)
    return redirect('/dashboard')


@app.route('/myMessages')
def showMessages():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    person_in_session = session['user_id']
    print(person_in_session) #person in session is the sender_id
    return render_template("myMessages.html", messages=Messages.get_all_messages(data), dtformat=realdate)

@app.route ('/delete_message/<int:id>')
def delete_message(id):
    data = {
        'id': id
    }
    print(data, "messagesssssssssss")
    Messages.delete_message(data)
    return redirect('/myMessages')