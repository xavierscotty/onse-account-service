from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Account(Base):
    __tablename__ = 'transactions'

    account_number = Column(Integer, primary_key=True, autoincrement=True)
    account_status = Column(String(100))
    customer_id = Column(String(50))

    @property
    def formatted_account_number(self):
        return format(self.account_number, '08')
