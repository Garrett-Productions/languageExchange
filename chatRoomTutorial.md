Python Live Chat Room Tutorial Using Flask & SocketIO

Installs
- flask, flask-socketio


As of now we are exporting and importing html templates, like we are using react, using the {% extends home.html%}


OVERVIEW OF WATCHTHROUGH
- sockets wasnt intemidating, we can socket.on, socket.off and socket.emit
- socket knows about 'connect' and 'disconnect'
- we are writing a very basic algo to generate a room code for each code of length(4)
- we are small kine passing error messages with jinja depending on the form error
- we can are storing the room, and the name of the user in session, and we can session.clear in our function call
- we are also deleting a chat room if there are no users
- we are time stamping our messages, and can prob create a cond to get rid of the timestamp if the browser has been refreshed
- we are storing our messages in memory
- In all, We aren't using that much JS, but I'm going to modularize it out in a script.src file