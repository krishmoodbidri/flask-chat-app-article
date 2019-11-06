from flask import Flask, render_template
from flask_socketio import SocketIO
import os
import sys
import time
global time_stamp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


directory = "/Users/krishmoodbidri/projects/test-flasl/flask-chat-app-article/db"
if not os.path.exists(directory):
            os.makedirs(directory)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('user connect')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
    time_stamp = time.strftime("%m-%d-%Y_%H:%M:%S")
    complete_file_name = os.path.join(directory, time_stamp + ".txt")
    file = open(complete_file_name, "w")
    file.close()
    time.sleep( 5 )


    pre, ext = os.path.splitext(complete_file_name)
    os.rename(complete_file_name, pre + ".done")
    socketio.emit('create response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)
