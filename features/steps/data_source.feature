 Feature: Telecom Data Source Management
  As a developer working with telecom data
  I want to use different data sources for telecom information
  So that I can have up-to-date and accurate data

  Background:
    Given the TelecomFaker package is installed

  Scenario: Use default static data source
    When I create a TelecomFaker instance with default settings
    Then it should use the static JSON data source
    And I should be able to generate valid operator information

  Scenario: Fallback to static data when data source is unavailable
    Given the data source is unavailable
    When I request a random operator
    Then I should receive an appropriate error message
    And the error should suggest checking the data source