Feature: Telecom Operator Data Generation
  As a telecom test engineer
  I want to generate realistic mobile operator data
  So that I can create authentic test scenarios for network applications

  Background:
    Given I have access to the TelecomFaker library

  Scenario: Generate random operator data for testing
    When I need a random telecom operator for my test
    Then I should receive complete operator information
    And the data should include essential operator identifiers
    And the data should include operator characteristics

  Scenario: Create reproducible test data sets
    Given I need predictable test data across multiple test runs
    When I use the same seed value for each test run
    Then I should get identical operator data each time
    And I can rely on this consistency for automated testing