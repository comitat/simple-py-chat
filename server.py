from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World"


@app.route("/status")
def status():
    current_time = time.asctime()
    return{
        'status': True,
        'name': 'simple messenger',
        'time': current_time
    }

app.run()