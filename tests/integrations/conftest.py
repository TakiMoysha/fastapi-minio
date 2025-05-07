from typing import Any, Generator
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client() -> Generator[TestClient, Any, None]:
    from app.main import application

    yield TestClient(application)
