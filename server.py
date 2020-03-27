from flask import Flask, request, abort
import datetime
import time

app = Flask(__name__)

messages = [
    {'username': 'user1', 'text':'Hello', 'time': 0.0}

]

users = {
    'user1':"123456"
}

@app.route("/")
def hello():
    return "Hello, World"


@app.route("/status")
def status():
    return{
        'status': True,
        'name': 'simple messenger',
        'time': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        'messages_count': len(messages),
        'users_count': len(users)
    }

@app.route("/send", methods=['POST'])
def send():
    username = request.json['username']
    password = request.json['password']

    if username in users:   #зарегестрированный пользователь
        if password != users[username]:
            return abort(401)
    else:                   #новый пользователь: регистрируем
        users[username] = password

    text = request.json['time']
    current_time = time.time()
    message = {'username':username, 'text':text, 'time':current_time}
    messages.append(message)

    print(messages)
    return {"ok": True}

@app.route("/messages")
def messages_view():
    after = float(request.args.get('after'))
    # filtered_massages = []
    # for message in messages:
    #     if message['time'] > after:
    #         filtered_massages.append(message)
    filtered_massages = [message for message in messages if message['time'] > after]

    return {
        'messages': filtered_massages
    }

app.run()