
class Account:

    account_list = []
    
    def __init__(self, account_name, account_userName, account_password):

        self.account_name = account_name
        self.account_userName = account_userName
        self.account_password = account_password


    def save_account(self):
        Account.account_list.append(self)


    # @classmethod
    # def display_accounts(cls):
    #     return cls.account_list


    # def delete_account(self):
    #     Account.account_list.remove(self)


    # @classmethod
    # def find_by_accountName(cls,accountname):
    #     for account in cls.account_list:
    #         if account.account_name == accountname:
    #             return account
