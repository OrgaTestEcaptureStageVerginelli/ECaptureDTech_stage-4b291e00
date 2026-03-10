"""Integration tests for the FastAPI application."""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint() -> None:
    """Test the root path"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"


def test_flow_add_and_list() -> None:
    """Tests the 2 endpoints for the methods add_task and get_all_list"""
    client.post("/tasks/add?title=Refactor&priority=Medium")
    response = client.get("/tasks/list")
    assert response.status_code == 200
    assert any(task["title"] == "Refactor" for task in response.json())


def test_discount_endpoint() -> None:
    """Tests the endpoint for the function calculate_discount"""
    response = client.get("/calculate/discount?price=100.0&discount=20.0")
    assert response.status_code == 200
    data = response.json()
    assert data["final_price"] == 80.0
    assert data["original_price"] == 100.0
    assert data["discount_applied"] == 20.0
