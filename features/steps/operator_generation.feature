Feature: Telecom Operator Data Generation
  As a developer working with telecom data
  I want to generate realistic telecom operator test data
  So that I can create meaningful test scenarios for my applications

  Background:
    Given the TelecomFaker package is installed
    And the telecom data source is available

  Scenario: Generate a random telecom operator
    When I request a random telecom operator
    Then I should receive valid operator information
    And the information should include name, country, MCC, and MNC
    And the information should include size and MVNO status

  Scenario: Handle non-existent operator
    When I request an operator with name "NonExistentOperator"
    Then I should receive an appropriate error message

  Scenario: Handle non-existent country
    When I request an operator from "NonExistentCountry"
    Then I should receive an appropriate error message

  Scenario: Generate consistent data with seed
    Given I set a random seed of 42
    When I request a random operator twice
    Then I should receive the same operator information both times 