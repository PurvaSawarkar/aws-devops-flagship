def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'healthy'}


def test_ready(client):
    response = client.get('/ready')
    assert response.status_code == 200
    assert response.json() == {'status': 'ready'}


def test_task_crud(client):
    create_response = client.post(
        '/tasks',
        json={
            'title': 'Learn AWS',
            'description': 'Build a DevOps portfolio project',
        },
    )
    assert create_response.status_code == 201

    task = create_response.json()
    task_id = task['id']
    assert task['title'] == 'Learn AWS'
    assert task['completed'] is False

    list_response = client.get('/tasks')
    assert list_response.status_code == 200
    assert any(item['id'] == task_id for item in list_response.json())

    get_response = client.get(f'/tasks/{task_id}')
    assert get_response.status_code == 200
    assert get_response.json()['title'] == 'Learn AWS'

    update_response = client.patch(
        f'/tasks/{task_id}',
        json={'completed': True},
    )
    assert update_response.status_code == 200
    assert update_response.json()['completed'] is True
    assert update_response.json()['title'] == 'Learn AWS'

    delete_response = client.delete(f'/tasks/{task_id}')
    assert delete_response.status_code == 204

    missing_response = client.get(f'/tasks/{task_id}')
    assert missing_response.status_code == 404


def test_empty_title_rejected(client):
    response = client.post('/tasks', json={'title': ''})
    assert response.status_code == 422


def test_missing_task_returns_404(client):
    response = client.get('/tasks/999999')
    assert response.status_code == 404


def test_task_pagination(client):
    response = client.get('/tasks?limit=1&offset=0')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
