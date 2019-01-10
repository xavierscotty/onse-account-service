from account_service.api.accounts import AccountNotFound


class MockAccountRepository:
    def __init__(self):
        self.accounts = {}
        self.last_account_number = 0

    def store(self, account):
        account_number = self._generate_account_number()
        account_copy = account.copy()
        account_copy['accountNumber'] = account_number
        self.accounts[account_number] = account_copy

        return account_number

    def fetch_by_account_number(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFound

        return self.accounts[account_number]

    def _generate_account_number(self):
        self.last_account_number = self.last_account_number + 1
        return format(self.last_account_number, '08')
