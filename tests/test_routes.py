<<<<<<< HEAD
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['message'] == 'Hello, World!'

def test_echo(client):
    message = "Hello"
    rv = client.get(f'/echo/{message}')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['message'] == message
=======
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['message'] == 'Hello, World!'

def test_echo(client):
    message = "Hello"
    rv = client.get(f'/echo/{message}')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['message'] == message
>>>>>>> 383a55dab16c3c6b2eb3e0ff1b362f6ccf4b9ca8
