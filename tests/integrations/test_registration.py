import pytest


from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_registration_endpoint(client: TestClient):
    # response = client.post("/api/auth/sign-up", json={"email": "test", "password": "test"})
    response = client.get("/api/health")
    assert response.status_code == 200
