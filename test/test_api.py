import flask
import flask.testing
from pytest import fixture

from flask_app.app import app


class TestApi:

    @fixture
    def test_app(self) -> flask.testing.FlaskClient:
        return app.test_client()

    def test_there_should_be_an_endpoint_which_returns_hello_world(self, test_app: flask.testing.FlaskClient):
        res = test_app.get('/hello')
        assert res.status_code == 200
        assert b'Hello World!' == res.data

    def test_any_random_endpoint_if_hit_should_return_404(self, test_app: flask.testing.FlaskClient):
        res = test_app.get('/uisgbre')
        assert res.status_code == 404
