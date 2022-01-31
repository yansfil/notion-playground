import pytest

from src.notion.endpoints.databases import DatabaseModel
from src.notion.service import NotionService


@pytest.fixture
def db_id():
    """
        개인 계정(grab)에서 사용하는 test_db_id
    :return: str
    """
    return "eda917e17e674054865d44d998343ed6"


def test_notion_svc(notion):
    assert isinstance(notion, NotionService)


def test_notion_retrieve_database(notion, db_id):
    response = notion.databases.retrieve(id=db_id)
    assert response


def test_notion_query_database(notion, db_id):
    database = notion.databases.query(id=db_id)
    assert isinstance(database, DatabaseModel)
