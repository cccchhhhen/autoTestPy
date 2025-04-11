from utils.http_client import HttpClient

def test_demo():
    client = HttpClient()
    r = client.post("/login", {"username": "admin","password": "admin"})
    assert r.status_code == 200
