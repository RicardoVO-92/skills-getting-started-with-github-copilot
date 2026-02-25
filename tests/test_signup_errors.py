from urllib.parse import quote


def test_signup_nonexistent_activity_returns_404(client):
    res = client.post(f"/activities/{quote('No Such Activity')}/signup", params={"email": "a@b.com"})
    assert res.status_code == 404


def test_signup_duplicate_returns_400(client):
    # michael@mergington.edu is pre-seeded in Chess Club
    activity = "Chess Club"
    existing = "michael@mergington.edu"
    res = client.post(f"/activities/{quote(activity)}/signup", params={"email": existing})
    assert res.status_code == 400
