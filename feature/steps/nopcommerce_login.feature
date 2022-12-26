Feature: Test login functionality
  Scenario: Login to dashboard page with valid credentials
    Given I launch Chrome browser
    When I open Nopcommerce login page
    And Enter email "admin@yourstore.com" and password "admin"
    And Click on Login button
    Then Login must be successful

