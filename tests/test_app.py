import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, Docker CI/CD! from Timokhin V.M.'


def test_api_sum(client):
    response = client.get("/api/sum/5/7")
    
    assert response.status_code == 200
    # Получаем данные сразу в формате JSON
    json_data = response.get_json()
    assert json_data["result"] == 12, "Калькулятор посчитал неверно"

def test_404_page(client):
    response = client.get("/non-existent")
    
    assert response.status_code == 404