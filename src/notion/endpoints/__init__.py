import abc
from typing import Optional

import httpx as httpx
from pydantic.main import BaseModel

from src import HttpRequest
from src.client import HttpClient
from src.types import Id


class Parent(BaseModel):
    ...


class Properties(BaseModel):
    ...


class RequestDTO(BaseModel):
    parent: Optional[Parent] = None
    properties: Optional[Properties] = None


class NotionDomain(BaseModel):
    ...


class NotionEndpoint(abc.ABC):
    path_prefix = ""

    def __init__(self, client: HttpClient):
        self.client = client

    @abc.abstractmethod
    def retrieve(self, id: Id) -> NotionDomain:
        ...

    @abc.abstractmethod
    def update(self, body: RequestDTO) -> NotionDomain:
        ...

    @abc.abstractmethod
    def create(self, body: RequestDTO) -> NotionDomain:
        ...
