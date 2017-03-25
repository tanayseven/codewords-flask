from injector import Injector

from flask_app.repos import AccountRepository


from flask_app.modules import ProdDatabaseModule

class Account(object):

    def __init__(self, user_name='', full_name='', balance=0, injector=Injector([ProdDatabasegiModule])):
        self.__repo = injector.get(AccountRepository)
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

    def login(self, user_name, password):
        return self.__repo.account_exists(user_name, password)
