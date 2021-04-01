import requests

url = 'http://127.0.0.1:8000/display_person/1'
myobj = {'first_name': 'George'}

x = requests.post(url, data = myobj)

print(x.text)