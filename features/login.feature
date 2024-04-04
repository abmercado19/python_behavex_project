# Created by anita at 21/03/2024
Feature: Login
  # This feature is going to be used for all the tests related to login and creation of new accounts

  Scenario: I can login into the Tools QA page with an existing user and correct password
    Given I open the Tools QA page
    When I complete the user name field with testing user name
    And I complete the password field with testing user password
    And I click the Login button
    Then I see the profile page is displayed
    And I see the user name is displayed in the page
