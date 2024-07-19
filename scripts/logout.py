from requests import post
from random import choice
from string import ascii_lowercase
from sys import argv

HOST = "http://localhost:5173"

resp = post(
    HOST + "/api/v1/auth/logout/",
    data={},
    headers={"Authorization": f"Token {argv[1]}"},
)

print(resp.content)
