from pydantic.env_settings import BaseSettings
from pydantic.fields import Field
from pydantic.main import BaseModel


class NotionOptions(BaseSettings):
    api_key: str = Field(..., env="NOTION_API_KEY")


class NotionDatabase(BaseModel):
    def to_iterable(self):
        return []


class NotionService:
    def __init__(self, options: NotionOptions):
        self.options = options

    def get_db(self):
        return NotionDatabase()
