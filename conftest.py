import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope='function')
def client():
    from app import app
    client = TestClient(app)
    return client
