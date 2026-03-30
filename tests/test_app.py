from app import create_app

def test_health_check():
    app = create_app()
    app.testing = True
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_calories_success():
    app = create_app()
    app.testing = True
    client = app.test_client()
    response = client.get('/calories/70/FL')
    assert response.json["calories"] == 1540

def test_calories_invalid_program():
    app = create_app()
    app.testing = True
    client = app.test_client()
    response = client.get('/calories/70/XYZ')
    assert response.status_code == 400