class AccountRepository(object):

    def __init__(self, initial_data=[]):
        if initial_data == []:
            self.__account_info = [
                {
                    'user_name': 'tanay',
                    'password': '1234',
                    'full_name': 'Tanay PrabhuDesai',
                },
                {
                    'user_name': 'tushar',
                    'password': '2222',
                    'full_name': 'Tushar Jarhad',
                },
                {
                    'user_name': 'piyush',
                    'password': '6666',
                    'full_name': 'Piyush Katariya',
                }
            ]
        else:
            self.__account_info = initial_data

    def get_list_of_accounts(self) -> list:
        return self.__account_info

    def add_accounts(self, account: dict):
        self.__account_info.append(account)

    def account_exists(self, user_name, password):
        return any([
            user_name == account['user_name'] and password == account['password']
            for account in self.__account_info
        ])

