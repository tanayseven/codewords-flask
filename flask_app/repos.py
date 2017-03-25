from flask_app.account import Account


class AccountRepository(object):

    def get_all_account(self):
        return [Account(user_name='tanay PrabhuDesai'), Account(user_name='tushar')]

