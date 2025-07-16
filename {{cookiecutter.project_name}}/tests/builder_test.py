from collections.abc import Mapping
from typing import Any, Optional

import pytest
from routelit import PropertyDict, RouteLitRequest

from {{cookiecutter.project_slug}}.builder import RLBuilder


class MockRLRequest(RouteLitRequest):
    def __init__(
        self,
        headers: Mapping[str, str] = {},
        path_params: Mapping[str, Any] = {},
        referrer: Optional[str] = None,
        is_json: bool = True,
        json: Optional[dict[str, Any]] = None,
        query_params: Mapping[str, str] = {},
        query_param_list: Mapping[str, list[str]] = {},
        session_id: str = "123",
        pathname: str = "/test",
        host: str = "localhost",
        method: str = "GET",
    ):
        self.headers = headers
        self.path_params = path_params
        self.referrer = referrer
        self._is_json = is_json
        self.json = json
        self.query_params = query_params
        self.query_param_list = query_param_list
        self.session_id = session_id
        self.pathname = pathname
        self.host = host
        self._method = method

    def get_headers(self) -> dict[str, str]:
        return self.headers

    def get_path_params(self) -> Optional[Mapping[str, Any]]:
        return self.path_params

    def get_referrer(self) -> Optional[str]:
        return self.referrer

    def is_json(self) -> bool:
        return self._is_json

    def get_json(self) -> Optional[dict[str, Any]]:
        return self.json

    def get_query_param(self, key: str) -> Optional[str]:
        return self.query_params.get(key)

    def get_query_param_list(self, key: str) -> list[str]:
        return self.query_param_list.get(key, [])

    def get_session_id(self) -> str:
        return self.session_id

    def get_pathname(self) -> str:
        return self.pathname

    def get_host(self) -> str:
        return self.host

    @property
    def method(self) -> str:
        return self._method


class TestRLBuilder:
    @pytest.fixture
    def mock_request(self) -> MockRLRequest:
        return MockRLRequest(method="POST")

    @pytest.fixture
    def builder(self, mock_request: MockRLRequest) -> RLBuilder:
        return RLBuilder(request=mock_request, session_state=PropertyDict({}), fragments={})

    def test_hello_world(self, builder: RLBuilder) -> None:
        builder.hello_world()
        builder.hello("routelit")

        elements = builder.get_elements()
        assert len(elements) == 2
        assert elements[0].name == "hello"
        assert elements[0].props["name"] == "world"
        assert elements[1].name == "hello"
        assert elements[1].props["name"] == "routelit"
