Feature: Create account
    As a customer
    I want to create an account
    In order to have a safe place to keep my money

    Scenario: An account is created successfully
        Given I am a registered customer with ID "12345"
        When I create an account with customer ID "12345"
        Then my account should be "active" and have customer ID "12345"

    Scenario: Customer does not exist
        Given there is no customer with ID "56789"
        When I create an account with customer ID "56789"
        Then then account should not be created
