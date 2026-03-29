from app import app

def test_health_check():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_calories_success():
    client = app.test_client()
    response = client.get('/calories/70/FL')
    assert response.json["calories"] == 1540

def test_calories_invalid_program():
    client = app.test_client()
    response = client.get('/calories/70/XYZ')
    assert response.status_code == 400