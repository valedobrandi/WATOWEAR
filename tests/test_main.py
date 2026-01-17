import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

# 1. Test the Health Check
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

# 2. Test the Outfit Generation (Mocked AI)
@patch("app.services.ai_service.ai_service.generate_outfit_recommendation")
def test_generate_outfit_success(mock_ai):
    # Setup what the "Fake AI" should return
    mock_ai.return_value = {
        "outfit_name": "Mocked Summer Chic",
        "selected_items": ["White T-shirt", "Blue Jeans"],
        "style_advice": "Great for a sunny day!"
    }

    # The payload we send to our API
    payload = {
        "clothes": ["White T-shirt", "Blue Jeans", "Black Hoodie"],
        "occasion": "Casual outing",
        "weather": "Sunny 25°C",
        "style": "Minimalist"
    }

    response = client.post("/generate-outfit", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["outfit_name"] == "Mocked Summer Chic"
    assert "White T-shirt" in data["selected_items"]

# 3. Test Validation Error (Empty wardrobe)
def test_generate_outfit_invalid_data():
    # Sending an empty list of clothes should trigger Pydantic validation
    payload = {
        "clothes": [], 
        "occasion": "Gym",
        "weather": "Hot",
        "style": "Sporty"
    }
    response = client.post("/generate-outfit", json=payload)
    assert response.status_code == 422 # Unprocessable Entity