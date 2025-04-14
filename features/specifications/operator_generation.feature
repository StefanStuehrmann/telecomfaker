Feature: Telecom Operator Data Generation
  As a developer working with telecom data
  I want to generate realistic telecom operator test data
  So that I can create meaningful test scenarios for my applications

  Background:
    Given the TelecomFaker module is initialized
    And the telecom data source is loaded

  Scenario: Generate a random telecom operator
    When I request a random telecom operator
    Then I should receive valid operator information
    And the information should include name, country, MCC, and MNC
    And the information should include size and MVNO status