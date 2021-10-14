import requests

API_URL = "http://localhost:5000/"

r = requests.get(API_URL + "profiles", data={'username':"bob"})
print(r.json())