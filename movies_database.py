import urllib.request
import json
import os
import helpers


if __name__ == '__main__':
    api_key = os.environ.get('TMDB_key')
    movies_database = []
    first_movie_id = 2
    last_movie_id = 32

    for movie_id in range(first_movie_id, last_movie_id):
        try:
            movies_database.append(helpers.make_tmdb_api_request(
                method='/movie/%s' % movie_id,
                api_key=api_key))
        except urllib.error.HTTPError:
            pass

    with open('movies_database.json', 'w') as f_obj:
        json.dump(movies_database, f_obj)

    print(movies_database)
