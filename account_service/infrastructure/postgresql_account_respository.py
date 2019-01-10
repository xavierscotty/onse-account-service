from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from account_service.api.accounts import AccountNotFound


class PostgreSQLAccountRepository:
    def __init__(self, host, port, username, password, db):
        url = f'postgresql://{username}:{password}@{host}:{port}/{db}'
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def store(self, account_hash):
        account = Account(account_status=account_hash['accountStatus'],
                          customer_id=account_hash['customerId'])
        self.session.add(account)
        self.session.commit()

        return format(account.account_number, '08')

    def fetch_by_account_number(self, account_number):
        accounts = self.session \
            .query(Account) \
            .filter(Account.account_number == account_number)

        if len(accounts) == 0:
            raise AccountNotFound

        account = accounts[0]

        return {'accountNumber': account.account_number,
                'accountStatus': account.account_status,
                'customerId': account.customer_id}


Base = declarative_base()


class Account(Base):
    __tablename__ = 'transactions'

    account_number = Column(Integer, primary_key=True, autoincrement=True)
    account_status = Column(String(100))
    customer_id = Column(String(50))
