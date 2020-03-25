import requests
import time

def get_message():
    response = requests.get('http://127.0.0.1:5000/messages')
    data = response.json()
    return data['messages']
    
while True:
    print(get_message())

    time.sleep(1)