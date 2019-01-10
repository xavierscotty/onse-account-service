import pytest

from account_service.api.accounts import AccountNotFound


def test_store_returns_a_account_number_as_8_digits(account_repository):
    account = {'customerId': '12345', 'accountStatus': 'active'}
    account_number = account_repository.store(account)

    assert type(account_number) is str
    assert len(account_number) == 8


def test_store_generates_a_new_account_number_each_time(account_repository):
    account = {'customerId': '12345', 'accountStatus': 'active'}
    account_number1 = account_repository.store(account)
    account_number2 = account_repository.store(account)

    assert account_number1 != account_number2


def test_fetch_by_account_number_raises_if_not_found(account_repository):
    with pytest.raises(AccountNotFound):
        account_repository.fetch_by_account_number('12345678')


def test_fetch_by_account_number_does_not_modify_the_input(account_repository):
    account = {'customerId': '12345', 'accountStatus': 'active'}
    account_repository.store(account)
    assert 'accountNumber' not in account


def test_fetch_by_account_number_returns_the_account(account_repository):
    account_number = account_repository.store({'customerId': '12345',
                                               'accountStatus': 'active'})
    account_repository.store({'customerId': '99999', 'accountStatus': 'active'})

    account = account_repository.fetch_by_account_number(account_number)

    expected = {'customerId': '12345',
                'accountNumber': account_number,
                'accountStatus': 'active'}

    assert account == expected, f'{repr(account)} != {repr(expected)}'
