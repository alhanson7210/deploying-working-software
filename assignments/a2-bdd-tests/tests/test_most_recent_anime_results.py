import requests
import pytest
from pytest_bdd import scenarios, when, then
from datetime import date

ANIME_SEARCH_API_PATH = "https://api.jikan.moe/v3/search/anime?q=&page=1&genre=1,10&order_by=start_date&sort=desc"
FEATURE = "../features/most_recent_anime_results.feature"
scenarios(FEATURE)

@pytest.fixture
@when('I search for the most recent Action&Fantasy anime')
def search_for_the_most_recent_anime_series():
    params = {'format': 'json'}
    response = requests.get(ANIME_SEARCH_API_PATH, params)
    return response

@then('the response status code should be 200')
def query_response_status_code_is_ok(search_for_the_most_recent_anime_series):
    assert search_for_the_most_recent_anime_series.status_code == 200

@then('the last page should be at most 20')
def check_the_last_page_is_at_most_20_pages(search_for_the_most_recent_anime_series):
    response = search_for_the_most_recent_anime_series.json()
    last_page = int(response['last_page'])
    assert 20 >= last_page

@then('the list should at least contain the current year or the next')
def check_that_the_next_or_current_year_is_present(search_for_the_most_recent_anime_series):
    response = search_for_the_most_recent_anime_series.json()
    results = response['results']
    filtered_results = list(filter(lambda obj: obj['start_date'] != "null", results))
    current_year = int(date.today().year)
    c_year = str(current_year)
    next_year = current_year + 1
    n_year = str(next_year)
    length = len(results)
    expected = True
    actual = False
    for result in filtered_results:
        start_date = result['start_date']
        if n_year in start_date or c_year in start_date:
            actual = True
            break
    assert expected == actual
