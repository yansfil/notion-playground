import os

import httpx
import pytest
from dotenv import load_dotenv

from src.client import HttpClient, HttpOptions
from src.notion.service import NotionService

load_dotenv(verbose=True)


@pytest.fixture(scope="session")
def token():
    assert os.getenv("NOTION_API_KEY") is not None, "환경변수에 NOTION_API_KEY를 넣어주세요."
    return os.getenv("NOTION_API_KEY")


@pytest.fixture()
def http_options():
    return HttpOptions()


@pytest.fixture()
def http_client(http_options):
    client = HttpClient(options=http_options, client=httpx.Client())
    client.headers = {
        "Notion-Version": http_options.notion_version,
        "authorization": f"Bearer {http_options.auth_token}",
    }
    return client


@pytest.fixture()
def notion(http_client):
    return NotionService(client=http_client)
