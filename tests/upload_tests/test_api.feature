Feature: Rental API

  Scenario: Retrieve Rental Data
    Given Add request header to data dict
    When User request post connection endpoint
    Then User should get 200 status code

