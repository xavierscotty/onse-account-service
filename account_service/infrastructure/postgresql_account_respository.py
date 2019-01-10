from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from account_service.api.accounts import AccountNotFound
from account_service.domain.account import Account


class PostgreSQLAccountRepository:
    def __init__(self, host, port, username, password, db):
        url = f'postgresql://{username}:{password}@{host}:{port}/{db}'
        self.engine = create_engine(url)
        declarative_base().metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def store(self, account):
        self.session.add(account)
        self.session.commit()

    def fetch_by_account_number(self, account_number):
        accounts = self.session \
            .query(Account) \
            .filter(Account.account_number == account_number)

        if len(accounts) == 0:
            raise AccountNotFound

        return accounts[0]
