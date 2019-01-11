from unittest.mock import Mock

import pytest

from account_service.domain import commands
from account_service.domain.account import Account
from account_service.domain.errors import AccountNotFound, CustomerNotFound


def test_get_account_when_account_is_not_found(account_repository):
    with pytest.raises(AccountNotFound):
        commands.get_account(
            account_number='12345678',
            account_repository=account_repository)


def test_get_account_when_account_is_found(account_repository):
    account = Account(customer_id='1234', account_status='active')
    account_repository.store(account)
    account_number = account.account_number

    returned_account = commands.get_account(
        account_number=account_number,
        account_repository=account_repository)

    assert account == returned_account


def test_create_account_when_customer_not_found(customer_client):
    account_repository = Mock()
    account = Account(customer_id='12345', account_status='active')

    with pytest.raises(CustomerNotFound):
        commands.create_account(account=account,
                                account_repository=account_repository,
                                customer_client=customer_client)

    assert not account_repository.store.called


def test_create_account_stores_the_account(customer_client):
    account_repository = Mock()
    customer_client.add_customer_with_id('12345')
    account = Account(customer_id='12345', account_status='active')

    commands.create_account(account=account,
                            account_repository=account_repository,
                            customer_client=customer_client)

    account_repository.store.assert_called_with(account)
