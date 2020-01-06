def test_home(client):
    rv = client.get("/")
    assert rv.status_code == 302
    assert rv.headers["Location"].endswith("/tasks/")


def test_list_task(client):
    rv = client.get("/tasks/")
    assert rv.status_code == 200


def test_show_task(client):
    rv = client.get("/tasks/task-1/")
    assert rv.status_code == 200
    assert b"task1" in rv.data
    assert b"completed" in rv.data
    assert b"tests.task1(1, a=&#39;b&#39;)" in rv.data


def test_show_task_not_exists(client):
    rv = client.get("/tasks/task-not-exists/")
    assert rv.status_code == 404
