import pytest

from task_dashboard.server import create_app


@pytest.fixture
def client():
    test_config = {
        "TESTING": True,
        "TASK_LOGS_BACKEND": "task_logs.backends.StubBackend",
        "TASK_LOGS_OPTIONS": {},
        "TASK_LOGS_FAKEDATA": True,
    }

    app = create_app(test_config)

    with app.test_client() as client:
        client.app = app
        yield client
