import requests
import time

after = 0

def get_messages(after):
    response = requests.get('http://127.0.0.1:5000/messages',
    params={'after': after})
   
    data = response.json()
    return data['messages']
    

while True:
    messages = get_messages(after)
    print(messages)

    for message in messages:
        if message['time']  > after:
            after = message['time']

    time.sleep(1)