import httpx

def test_get_post():
    resp = httpx.get("https://jsonplaceholder.typicode.com/posts/1")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
