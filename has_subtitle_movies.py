import json
import helpers


if __name__ == '__main__':
    movies_database = helpers.load_json_data_from_json_package(
        'movies_database.json')

    user_search_subtitle = input()

    for movie in movies_database:
        if user_search_subtitle.lower() in movie['title'].lower():
            print(movie['title'])
