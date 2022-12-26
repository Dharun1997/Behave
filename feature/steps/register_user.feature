Feature: To register a new user successfully
  Background: Common steps
    Given Launch Chrome Browser
    When Login Page will be opened
    Then Dashboard page will be shown

  Scenario Outline: Register a new user
    Given Click on the Customers tab at the left side and select Customers option
    When Click on Add New option button
    And Enter mail "<mail>" firstname "<firstname>" lastname "<lastname>" dob "<dob>" in the corresponding fields
    And Click on Save button
    Then User must be successfully registered

    Examples:
      | mail               | firstname | lastname | dob |
      | madhesh3497@gmail.com | Madhesh    | Kasi | 11/5/2022 |