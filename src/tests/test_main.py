from fastapi.testclient import TestClient

from src.main import app

test_client = TestClient(app)

def test_api_healthchecker():
    responce = test_client.get('/api/healthchecker')
    assert responce.status_code == 200
    assert responce.json() == {
        'status': 'success',
        'message': 'Добро пожаловать в сервер FastAPI + MongoDB'
    }

def test_news_get():
    responce = test_client.get('/api/database/news?limit=5')
    assert responce.status_code == 200
    assert len(responce.json().get('news')) == 5
