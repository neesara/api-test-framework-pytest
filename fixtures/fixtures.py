import pytest
from api.api_client import APIClient
from utils.config import BASE_URL

@pytest.fixture
def api_client():
    return APIClient(BASE_URL)