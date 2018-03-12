import os
import helpers
api_key = os.environ.get('TMDB_key')

print(helpers.make_tmdb_api_request(
    '/movie/215',
    api_key=api_key)['budget'])
