from account_service.domain.errors import AccountNotFound


class MockAccountRepository:
    def __init__(self):
        self.accounts = {}
        self.last_account_number = 0

    def store(self, account):
        account.account_number = self._generate_account_number()
        self.accounts[account.account_number] = account

    def fetch_by_account_number(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFound

        return self.accounts[account_number]

    def _generate_account_number(self):
        self.last_account_number = self.last_account_number + 1
        return self.last_account_number
