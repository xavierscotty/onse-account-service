from account_service.domain.account import Account


def test_formatted_account_number():
    account = Account(account_number=1,
                      account_status='active',
                      customer_id='12345')

    assert account.formatted_account_number == '00000001'


def test_formatted_account_number_when_no_number():
    account = Account(account_status='active',
                      customer_id='12345')

    assert account.formatted_account_number is None
