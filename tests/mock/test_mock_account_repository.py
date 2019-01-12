import pytest

from account_service.domain.errors import AccountNotFound
from account_service.domain.account import Account


def test_store_sets_the_account_number_to_an_integer(account_repository):
    account = Account(customer_id='12345', account_status='active')
    account_repository.store(account)

    assert type(account.account_number) is int


def test_store_generates_a_new_account_number_each_time(account_repository):
    account1 = Account(customer_id='12345', account_status='active')
    account2 = Account(customer_id='12345', account_status='active')
    account_repository.store(account1)
    account_repository.store(account2)

    assert account1.account_number != account2.account_number


def test_fetch_by_account_number_raises_if_not_found(account_repository):
    with pytest.raises(AccountNotFound):
        account_repository.fetch_by_account_number(12345678)


def test_fetch_by_account_number_returns_the_account(account_repository):
    saved = Account(customer_id='12345', account_status='active')
    other = Account(customer_id='99999', account_status='active')
    account_repository.store(saved)
    account_repository.store(other)

    fetched = account_repository.fetch_by_account_number(saved.account_number)

    assert fetched is saved
