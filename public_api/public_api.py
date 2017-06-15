import requests

r = requests.get('https://jsonplaceholder.typicode.com/users/1')

print(r.json())
