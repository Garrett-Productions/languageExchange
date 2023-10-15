from flask_app.controllers import users, posts, user_languages, community_control, messages_control
from flask_app import app

if __name__=="__main__":
    app.run(debug=True, port = 5001) 