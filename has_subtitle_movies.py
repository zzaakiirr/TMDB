import urllib.request
import urllib.parse
import json


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)

with open('movies_database.json') as f_obj:
    movies_database = json.load(f_obj)

user_search_subtitle = input()

for movie in movies_database:
    if movie['title'].lower().find(
       user_search_subtitle.lower()) != -1:
        print(movie['title'])
