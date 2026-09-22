import responses


@responses.activate
def test_e2e_login_then_get_users(client):
    responses.add(responses.POST,
                  url="http://127.0.0.1:8000/api/login",
                  json={"code":200,"token":"t-123"},
                )
    responses.add(responses.GET,
                  url="http://127.0.0.1:8000/api/users",
                  json={"code":200,"users":[{"id":1,"name":"alice"},{"id":2,"name":"bob"}]},
                  match=[responses.matchers.header_matcher({"Authorization": "Bearer t-123"})]
                )
    client.login("alice", "t-123")
    resp = client.get_users()
    assert len(resp["users"]) == 2
