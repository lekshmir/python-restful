from resources.Users import app
import pytest


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_userauth_get(client):
    response = client.get('/login?user_name=Lekshmi&password=lechu')
    assert response.json['name'] == "Lekshmi"
    assert response.status_code == 200
    print(response.json)


def test_user_post_success(client):
    response = client.post('/user', query_string={'user_name': 'Hari', 'password': 'lechu', 'role_id': 1})
    assert response.status_code == 201


def test_user_post_failure(client):
    response = client.post('/user', query_string={'user_name': 'Lekshmi', 'password': 'lechu', 'role_id': 1})
    assert response.status_code == 409
    assert response.json['uid'] == 1


def test_user_post_missing_pwd(client):
    response = client.post('/user', query_string={'user_name': 'Oviya',  'role_id': 1})
    assert response.status_code == 400
    assert 'password' in response.json['message']
