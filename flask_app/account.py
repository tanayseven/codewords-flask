class Account(object):

    def __init__(self, user_name='', full_name='', balance=0):
        self.__user_name = user_name
        self.__full_name = full_name
        self.__balance = balance

    @property
    def user_name(self):
        return self.__user_name

    @property
    def full_name(self):
        return self.__full_name

    @property
    def balance(self):
        return self.__balance
