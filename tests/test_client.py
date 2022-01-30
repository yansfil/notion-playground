from src.http import HttpClient, HttpMethod, HttpOptions


def test_http_client_init(http_client):
    assert isinstance(http_client, HttpClient)


def test_http_client_request(http_client: HttpClient):
    result = http_client.request(
        method=HttpMethod.GET,
        path="/product",
    )
    assert result.status_code == 200
