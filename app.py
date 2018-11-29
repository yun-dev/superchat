from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room
import eventlet


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello super chat'
socketio = SocketIO(app)

messages = []


@socketio.on('connect')
def client_connected():
    pass


@socketio.on('chat')
def chat(msg):
    messages.append(msg)
    emit('chat', msg, broadcast=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat/')
def chat_html():
    return render_template('chat.html')


@app.route('/socketio_sample')
def socketio_sample():
    return render_template('socketio_client.html')


@app.route('/vue/')
def vue():
    return render_template('vue.html', message='hello, vue chat from flask server')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
