@smoke
Feature: Login

    Scenario Outline: Role-based login
        Given the user is on the login page
        When the user signs in as "<role>"
        Then the dashboard is shown

        Examples:
            | role      |
            | physician |
            | pharma    | 