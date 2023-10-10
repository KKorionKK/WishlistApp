import pytest
from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app=app)


@pytest.mark.asyncio
async def test_register_and_auth():
    registration_data = {
        "email": "demo@email.ru",
        "name": "Demo",
        "nickname": "DemoNickname",
        "password": "123",
        "gender": "М",
        "birthday": "2003-03-14T13:19:09.309Z",
    }
    response_registration = client.post(
        "/v1/authorization/register", content=json.dumps(registration_data)
    )
    assert response_registration.status_code == 200
    assert "access_token" in response_registration.json()

    login_data = {
        "username": registration_data.get("email"),
        "password": registration_data.get("password"),
    }
    response_login = client.post("/v1/authorization/token", data=login_data)
    assert response_login.status_code == 200
