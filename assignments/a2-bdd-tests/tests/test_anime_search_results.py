import pytest
import requests
from pytest_bdd import scenarios, when, then

ANIME_SEARCH_API_PATH = "https://api.jikan.moe/v3/search/anime?"

scenarios('../features/anime_search_results.feature',
          example_converters=dict(genre=int, order_by=str, limit=int))

@pytest.fixture
@when('the Jikan Api is queried with <genre>, <order_by>, <limit>')
def search_response(genre, order_by, limit):
    params = {'format': 'json'}
    formatted_path = "{}genre={}&order_by={}&limit={}" \
        .format(ANIME_SEARCH_API_PATH,
                genre,
                order_by,
                limit)
    response = requests.get(formatted_path, params)
    return response

@then('the response status code is 200')
def search_response_status_code_is_ok(search_response):
    assert search_response.status_code == 200

@then('the list of results is <limit>')
def search_response_results_size_is_limit(search_response, limit):
    response = search_response.json()
    results = response['results']
    assert limit == len(results)

@then('the list is organized by <order_by>')
def search_response_is_organized_by_order_by(search_response, order_by):
    response = search_response.json()
    results = response['results']
    length = len(results)
    expected = True
    actual = True
    for position in range(1, length):
        previous = results[position-1]
        current = results[position]
        previous_order_by = previous[order_by]
        current_order_by = current[order_by]
        if previous_order_by < current_order_by:
            actual = False
            break
    assert expected == actual
