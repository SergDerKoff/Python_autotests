import requests
import pytest

def test_statuscode():
    response = requests.get("https://petstore.swagger.io/v2/pet/123")
    assert response.status_code == 200

def test_string():
    response = requests.get("https://petstore.swagger.io/v2/pet/666")
    assert response.json()["name"] == "DEVIL"