from flask import Flask, request
import datetime
import time

app = Flask(__name__)

messages = [
    {'username': 'Jonh', 'text':'Hello', 'time': 0.0}

]

@app.route("/")
def hello():
    return "Hello, World"


@app.route("/status")
def status():
    return{
        'status': True,
        'name': 'simple messenger',
        'time': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }

@app.route("/send", methods=['POST'])
def send():
    username = request.json['username']
    text = request.json['time']
    current_time = time.time()
    message = {'username':username, 'text':text, 'time':current_time}
    messages.append(message)

    print(messages)
    return {"ok": True}

app.run()