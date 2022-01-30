from enum import Enum
from types import TracebackType
from typing import Optional, Type, Union

import httpx
from pydantic.fields import Field
from pydantic.main import BaseModel
from pydantic.networks import HttpUrl

from src.logger import create_logger
from src.types import DictType


class HttpOptions(BaseModel):
    base_url: HttpUrl = Field(env="NOTION_API_KEY")


class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class HttpClient:
    def __init__(
        self, options: HttpOptions, client: Union[httpx.Client, httpx.AsyncClient]
    ):
        self.options = options
        self.client = client
        self.logger = create_logger()

    def __enter__(self):
        self.client.__enter__()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        self.client.__exit__(exc_type, exc_value, traceback)

    def request(
        self,
        method: HttpMethod,
        path: str,
        query: Optional[DictType] = {},
        body: Optional[DictType] = {},
        headers: Optional[DictType] = {},
    ) -> httpx.Response:
        request = self._build_request(method, path, body, query, headers)

        self.logger.info(
            f"------REQUEST------"
            f"URL: {self.options.base_url}/{path}"
            f"METHOD: {method}"
            f"BODY: {body}"
            f"HEADERS: {headers}"
        )
        response = self.client.send(request=request)
        return response

    def _build_request(
        self,
        method: HttpMethod,
        path: str,
        query: Optional[DictType] = {},
        body: Optional[DictType] = {},
        headers: Optional[DictType] = {},
    ) -> httpx.Request:
        return self.client.build_request(
            method=method,
            url=f"{self.options.base_url}/{path}",
            params=query,
            json=body,
            headers=headers,
        )
