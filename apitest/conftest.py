import pytest

from apitest.clients.api_client import ApiClient

BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture
def client():
    return ApiClient(BASE_URL)