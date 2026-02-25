def test_root_redirects_to_static_index(client):
    # don't follow redirects so we can assert the redirect response
    res = client.get("/", follow_redirects=False)
    assert res.status_code in (301, 302, 307, 308)
    location = res.headers.get("location", "")
    assert location.endswith("/static/index.html")

    # Now fetch the static file
    static = client.get(location)
    assert static.status_code == 200
    ct = static.headers.get("content-type", "")
    assert "text/html" in ct
