from requests import post, get

HOST = 'http://localhost:5173'

resp = post(HOST + '/api/v1/auth/login/', data={
    'username': 'test',
    'password': 'test'
})
token = resp.json()['auth_token']

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
