from requests import post, get
from random import choice
from string import ascii_lowercase

HOST = 'http://127.0.0.1:8000'

resp = post(HOST + '/api/v1/auth/register/', data={
    'first_name': 'test',
    'last_name': 'test',
    'email': f'{"".join([choice(ascii_lowercase) for i in range(10)])}@test.test',
    'username': f'{"".join([choice(ascii_lowercase) for i in range(10)])}',
    'password': 'test'
})

print(resp.content)