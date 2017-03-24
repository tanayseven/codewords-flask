from flask_app.app import this_should_always_be_true


class TestExample:
    def test_this_test_should_pass(self):
        assert this_should_always_be_true()
