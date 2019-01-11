Feature: Get account details
    As a customer
    I want to get my account details
    In order to ensure I have an active account to keep my money safe

    Scenario: Getting details of an active account
        Given there an "active" account with customer id "12345"
        When I get the account details
        Then I should see an "active" account with customer id "12345"

    Scenario: Attempting to get account which doesn't exist
        Given there is no account with id "12345678"
        When I get the account details for account "12345678"
        Then I should get a not found message
