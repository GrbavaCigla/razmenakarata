from requests import post, get
from sys import argv

HOST = "http://localhost:5173"

resp = post(HOST + "/api/v1/auth/login/", data={"email": argv[1], "password": argv[2]})
token = resp.json()["auth_token"]

events = get(HOST + "/api/v1/events/").json()["results"]

for event in events:
    resp = post(
        HOST + f"/api/v1/events/{event["id"]}/tickets/",
        headers={"Authorization": f"Token {token}"},
        json={
            "price": 100,
            "amount": 1,
            "online": True,
            "package": event["packages"][0]["id"],
        },
    )
    break
