import pytest
import requests
from pytest_bdd import scenarios, when, then

ANIME_SEARCH_API_PATH = "https://api.jikan.moe/v3/search/anime?"
FEATURE = "../features/favorite_anime_search_results.feature"
scenarios(FEATURE, example_converters=dict(favorite_anime=str, limit=int, type=str, title=str))

@pytest.fixture
@when('I wish to search for my <favorite_anime> series with a limit of <limit> results')
def search_for_my_favorite_anime_series(favorite_anime, limit):
    params = {'format': 'json'}
    formatted_path = "{}q={}&limit={}" \
        .format(ANIME_SEARCH_API_PATH,
                favorite_anime,
                limit)
    response = requests.get(formatted_path, params)
    return response

@then('the response status code should be 200')
def query_response_status_code_is_ok(search_for_my_favorite_anime_series):
    assert search_for_my_favorite_anime_series.status_code == 200

@then('the list of results should be less than or equal to the <limit>')
def check_the_results_are_quantitatively_the_same_as_the_limit(search_for_my_favorite_anime_series, limit):
    response = search_for_my_favorite_anime_series.json()
    results = response['results']
    assert limit >= len(results)

@pytest.fixture
@then('I want to filter the results for a certain <series_type> from the series')
def filter_results_by_type(search_for_my_favorite_anime_series, series_type):
    response = search_for_my_favorite_anime_series.json()
    results = response['results']
    filtered_results = list(filter(lambda obj: obj['type'] == series_type, results))
    expected = True
    actual = True
    for result in filtered_results:
        if result['type'] != series_type:
            actual = False
            break
    return filtered_results if expected == actual else []

@then('from that list, I want to pick my favorite <title> to watch again')
def pick_favorite_title(filter_results_by_type, title):
    expected = title
    actual = ''
    for result in filter_results_by_type:
        if result['title'] == title:
            actual = result['title']
            break
    assert expected == actual
