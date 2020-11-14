import unittest
from user import User
from credentials import Account

class TestAccount(unittest.TestCase):
    def setUp(self):

        self.new_account = Account("Instagram", "Jack_Sparrow", "apirateslife")

    def test_init(self):
        self.assertEqual(self.new_account.account_name,"Instagram")
        self.assertEqual(self.new_account.account_userName,"Jack_Sparrow")
        self.assertEqual(self.new_account.account_password,"apirateslife")

    def test_save_account(self):
        self.new_account.save_account() #saving the new account
        self.assertEqual(len(Account.account_list),1)

    def tearDown(self):
        Account.account_list = []

    def test_display_account_credentials(self):
        self.assertEqual(Account.display_accounts(),Account.account_list)

    def test_delete_account(self):
        self.new_account.save_account()
        test_account = Account("Twitter", "James_Lebron", "basketballislife")
        test_account.save_account()

        test_account.delete_account()
        self.assertEqual(len(Account.account_list),1)

    def test_find_account_by_name(self):
        self.new_account.save_account()
        test_account = Account("Medium", "Jeff_Bezos", "investingissmart")
        test_account.save_account()

        found_account = Account.find_by_accountName("Medium")
        self.assertEqual(found_account.account_name,"Medium")



if __name__ == '__main__':
    unittest.main()