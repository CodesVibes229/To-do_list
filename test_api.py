import pytest
from app import create_app, db
from app.models import Task

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/test_db'

    with app.app_context():
        db.create_all()  # Créer les tables dans la base de données de test
        yield app
        db.drop_all()  # Nettoyer après les tests


@pytest.fixture
def client(app):
    return app.test_client()

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Nouvelle tâche'})
    assert response.status_code == 201
    assert 'Nouvelle tâche' in response.data.decode('utf-8')

def test_get_tasks(client):
    client.post('/tasks', json={'title': 'Nouvelle tâche'})
    response = client.get('/tasks')
    assert response.status_code == 200
    assert 'Nouvelle tâche' in response.data.decode('utf-8')

def test_update_task(client):
    response = client.post('/tasks', json={'title': 'Nouvelle tâche'})
    task_id = response.get_json()['id']
    response = client.put(f'/tasks/{task_id}', json={'title': 'Tâche mise à jour', 'done': True})
    assert response.status_code == 200
    assert 'Tâche mise à jour' in response.data.decode('utf-8')

def test_delete_task(client):
    response = client.post('/tasks', json={'title': 'Nouvelle tâche'})
    task_id = response.get_json()['id']
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 204
