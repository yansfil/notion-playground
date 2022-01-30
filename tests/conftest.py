import httpx
import pytest

from src.http import HttpClient, HttpOptions
from src.service.notion import NotionOptions


@pytest.fixture()
def http_options():
    return HttpOptions(base_url="https://www.notion.so")


@pytest.fixture()
def http_client(http_options):
    return HttpClient(options=http_options, client=httpx.Client())


@pytest.fixture()
def notion_options():
    return NotionOptions(api_key="TEST_API_KEY")
