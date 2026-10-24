# Gherkin tags like @smoke become pytest markers, so pytest -m smoke works.

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