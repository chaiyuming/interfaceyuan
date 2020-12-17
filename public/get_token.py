import json
import unittest
import requests

def get_token():
    url = "http://uathratt.zberpnc.com:8002/#/login"
    name = {"username": "fukaiyun", "password": "abcdefg123456"}
    login_data = requests.post(url, name)
    c = json.loads(login_data.text)["access-token"]
    token = {"access-token": c}
    return token

if __name__ == "__main__":
    print(get_token())