Feature: Telecom Data Source Management
  As a telecom test engineer
  I want to use different sources of telecom operator data
  So that I can create realistic test scenarios with accurate information

  Background:
    Given I have installed the TelecomFaker package

  Scenario: Use built-in telecom data for quick testing
    When I need to quickly generate telecom test data
    Then I should be able to use TelecomFaker without any configuration
    And it should provide realistic operator information out of the box

  Scenario: Handle unavailable data sources gracefully
    Given I am working in an environment with restricted network access
    When I try to generate telecom operator data
    Then I should receive a clear error message if data sources are unavailable
    And the error should help me troubleshoot the data source issue