from urllib.parse import quote


def test_signup_success_updates_state(client):
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # ensure email not present initially
    before = client.get("/activities").json()
    assert email not in before[activity]["participants"]

    # sign up
    res = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})
    assert res.status_code == 200
    assert "Signed up" in res.json().get("message", "")

    # verify state changed
    after = client.get("/activities").json()
    assert email in after[activity]["participants"]
