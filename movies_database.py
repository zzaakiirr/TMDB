import urllib.request
import urllib.parse
import json

api_key = os.environ.get('TMDB_key')


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

movies_database = []

for movie_id in range(2, 32):
    try:
        movies_database.append(make_tmdb_api_request(
            method='/movie/%s' % i,
            api_key=api_key))
    except urllib.error.HTTPError:
        pass


with open('movies_database.json', 'w') as f_obj:
    json.dump(movies_database, f_obj)

print(movies_database)
