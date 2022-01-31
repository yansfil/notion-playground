from src import HttpRequest
from src.client import HttpClient, HttpMethod


def test_http_client_init(http_client):
    assert isinstance(http_client, HttpClient)


def test_http_client_works(http_client):
    result = http_client.request(HttpRequest(method=HttpMethod.GET, path="users/me"))
    assert result.status_code == 200
