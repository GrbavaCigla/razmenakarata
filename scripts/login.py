from requests import post
from random import choice
from string import ascii_lowercase
from sys import argv

HOST = "http://localhost:5173"

resp = post(HOST + "/api/v1/auth/login/", data={
    "email": argv[1],
    # "email": f"{''.join([choice(ascii_lowercase) for i in range(10)])}@test.test",
    # "username": f"{''.join([choice(ascii_lowercase) for i in range(10)])}",
    "password": "Blablabla123",
})

print(resp.content)