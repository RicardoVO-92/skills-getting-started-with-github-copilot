from urllib.parse import quote


def test_unregister_nonexistent_activity_returns_404(client):
    res = client.delete(f"/activities/{quote('No Activity')}/signup", params={"email": "x@x.com"})
    assert res.status_code == 404


def test_unregister_nonmember_returns_404(client):
    activity = "Chess Club"
    email = "not-in-list@mergington.edu"
    res = client.delete(f"/activities/{quote(activity)}/signup", params={"email": email})
    assert res.status_code == 404
