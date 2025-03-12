from fastapi.testclient import TestClient

from {{cookiecutter.project_slug}}.server.main_app import app

client = TestClient(app)


def test_dev_foo():
    response = client.get("/dev/foo")
    assert response.status_code == 200
    assert response.json() == {"message": "foo"}
