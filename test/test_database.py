from pytest import fixture

from flask_app.repos import AccountRepository


class TestDatabase(object):

    @fixture
    def database(self):
        return AccountRepository()

    def test_account_repository_should_have_three_users_by_default(self, database: AccountRepository):
        list_of_accounts = database.get_list_of_accounts()
        assert len(list_of_accounts) == 3
        assert list_of_accounts[0]['user_name'] == 'tanay'
        assert list_of_accounts[1]['user_name'] == 'tushar'
        assert list_of_accounts[2]['user_name'] == 'piyush'

    def test_account_repository_should_have_four_usrs_after_we_add_a_user(self, database: AccountRepository):
        list_of_accounts = database.get_list_of_accounts()
        assert len(list_of_accounts) == 3
        database.add_accounts(dict(user_name='superman', password='zzzz', full_name='Clark Kent'))
        assert len(list_of_accounts) == 4
        assert list_of_accounts[3]['user_name'] == 'superman'

    def test_account_should_by_default_have_a_user_called_tushar(self, database: AccountRepository):
        success = database.account_exists('tushar', '2222')
        assert success

    def test_account_should_by_default_not_have_a_account_called_pandu(self, database: AccountRepository):
        success = database.account_exists('pandu', 'qwerty')
        assert not success
