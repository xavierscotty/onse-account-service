def test_has_customer_with_id(customer_client):
    customer_client.add_customer_with_id('1234')

    assert customer_client.has_customer_with_id('1234') is True
    assert customer_client.has_customer_with_id('5678') is False
