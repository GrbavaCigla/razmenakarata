from requests import post, get

HOST = 'http://127.0.0.1:8000'

resp = post(HOST + '/api/v1/auth/token/', data={
    'username': 'test',
    'password': 'test'
})
token = resp.json()['access']

count = len(get(HOST + '/api/v1/events/').json()["results"])

for i in range(count):
    resp = post(
        HOST + f'/api/v1/events/{i}/tickets/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'price': 100,
            'amount': 1,
            'online': True,
            'package': 'Lorem ipsum'
        }
    )
