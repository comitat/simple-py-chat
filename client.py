import requests

response = requests.get('http://127.0.0.1:5000/status')
print(response.status_code)
print(response.text)
print(response.json())

message = {'username': '0', 'text': '123'}

response = requests.post('http://127.0.0.1:5000/status', json=message) #{''})
print(response.status_code)
print(response.text)
print(response.json())