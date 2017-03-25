from doubles import allow, expect


class User(object):
    """
    Simple User
    """

    def __init__(self, name=""):
        self.name = name

    def get_name(self):
        """
        Get User name
        """
        return self.name

    def set_name(self, name):
        """
        Set User name
        """
        self.name = name


class SmsGateway(object):

    def __init__(self):
        pass

    def send_sms(self, user, message):
        pass


class View(object):
    """
    Sample operations on User
    """
    def __init__(self, user, sms_gateway):
        self.user = user
        self.sms_gateway = sms_gateway

    def greet_user(self):
        name = self.user.get_name()
        return "Hello " + name

    # Comment this function and run tests
    def send_sms(self, message):
        # Comment following line and run tests to understand difference between allow & expect
        self.sms_gateway.send_sms(self.user, message)
        return None


def test_user_name():
    user = User('sherlock')
    assert user.get_name() == 'sherlock'


def test_greet_user():
    user = User()
    view = View(user, None)
    allow(user).get_name.and_return('sherlock')
    message = view.greet_user()
    assert message == "Hello sherlock"


# Is this test helpful ?
def test_send_sms_using_allow():
    sms_gateway = SmsGateway()
    user = User()
    view = View(user, sms_gateway)
    allow(sms_gateway).send_sms
    view.send_sms("welcome")


def test_send_sms_mock():
    sms_gateway = SmsGateway()
    user = User()
    view = View(user, sms_gateway)
    # user2 = User("1")
    # view = View(user2, sms_gateway)
    # expect(sms_gateway).send_sms
    expect(sms_gateway).send_sms(user, "welcome")
    view.send_sms("welcome")


# allowance
# A declaration that one of an object's methods can be called. This is the manner by which stubs are created.
# expectation
# A declaration that one of an object's methods must be called. This is the manner by which mocks are created.
