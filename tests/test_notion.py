from src.service.notion import NotionService


def test_notion_get_db(notion_options):
    notion_svc = NotionService(options=notion_options)
    database = notion_svc.get_db()
    assert len(database.to_iterable()) == 0
