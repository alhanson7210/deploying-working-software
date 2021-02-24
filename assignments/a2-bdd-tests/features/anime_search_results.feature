Feature: Top Anime Search List For A Specific Genre
  As an active online anime enthusiast,
  I want to search for a list of anime for a specific genre ordered by their score,
  So that I know what is the best shows to watch first.

  Scenario Outline: Anime Searches with Jikan Api Query
    When the Jikan Api is queried with <genre>, <order_by>, <limit>
    Then the response status code is 200
    And the list of results is <limit>
    And the list is organized by <order_by>

    Examples: Queries
      | genre  | order_by | limit |
      | 1      | score    | 3     |
      | 2      | episodes | 5     |
      | 4      | members  | 10    |
