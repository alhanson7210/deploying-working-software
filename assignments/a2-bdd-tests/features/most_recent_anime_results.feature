Feature: Most popular anime results
  As a seasoned anime binge watcher,
  I want to search for a list of the most recent Action&Fantasy anime,
  So that I know which new anime I would end up watching

  Scenario: Fixed Search Results
    When I search for the most recent Action&Fantasy anime
    Then the response status code should be 200
    And the last page should be at most 20
    But the list should at least contain the current year or the next