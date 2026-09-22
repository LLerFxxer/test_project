import pytest
import requests
import responses


@responses.activate
def test_client(client):
    responses.add(responses.POST,
                  url="http://127.0.0.1:8000/api/login",
                  json={"code":200,"token":"t-123"},
                )
    responses.add(responses.GET,
                  url="http://127.0.0.1:8000/api/users",
                  json={"code":200,"users":[{"id":1,"name":"alice"},{"id":2,"name":"bob"}]},
                  match=[responses.matchers.header_matcher({"Authorization": "Bearer t-123"})])
    client.login("alice", "123456")
    resp = client.get_users()
    assert len(resp["users"]) == 2

@responses.activate
def test_timeout(client):
    responses.add(responses.GET,
                  url="http://127.0.0.1:8000/api/users",
                  body=requests.exceptions.Timeout("boom"),
                  status=500)
    with pytest.raises(requests.exceptions.Timeout):
        client.get_users()