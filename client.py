import requests

def send_message(username, text):
    message = {'username': username, 'text': text}
    response = requests.post('http://127.0.0.1:5000/send', json=message)
    return response.status_code ==200
    #if response.status_code == 200
    #   return True
    #else:
    #    return False

username = input('Your Name:')

while True:
    text =input('Your Massage:')
    result = send_message(username,text)
    if result is False:
        print('Error')