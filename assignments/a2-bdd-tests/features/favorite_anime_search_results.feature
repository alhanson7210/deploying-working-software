Feature: Favorite Anime Search Results
  As an avid anime watcher,
  I want to search for my favorite anime,
  So that I can relive the experience by re-watching my favorite series.

  Scenario Outline: Search For My Favorite Anime
    When I wish to search for my <favorite_anime> series with a limit of <limit> results
    Then the response status code should be 200
    And the list of results should be less than or equal to the <limit>
    And I want to filter the results for a certain <series_type> from the series
    And from that list, I want to pick my favorite <title> to watch again

    Examples: Search preferences
      | favorite_anime | limit | series_type  | title                          |
      | fairy tail     | 10    | Movie        | Fairy Tail Movie 2: Dragon Cry |
