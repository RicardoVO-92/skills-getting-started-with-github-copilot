from urllib.parse import quote


def test_unregister_success_removes_participant(client):
    activity = "Basketball Team"
    email = "alex@mergington.edu"

    # ensure participant exists initially
    before = client.get("/activities").json()
    assert email in before[activity]["participants"]

    # unregister
    res = client.delete(f"/activities/{quote(activity)}/signup", params={"email": email})
    assert res.status_code == 200
    assert "Unregistered" in res.json().get("message", "")

    # verify removed
    after = client.get("/activities").json()
    assert email not in after[activity]["participants"]
