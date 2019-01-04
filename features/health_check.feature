Feature: Health check
  As a automated service
  I want to be able to check that the service is running
  In order to ensure that a reasonable response is taken during failure

  Scenario: Everything is OK
    When I check the health of the service
    Then I should receive an OK response