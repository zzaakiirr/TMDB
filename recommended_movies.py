import urllib.request
import urllib.parse
import json

with open('movies_database.json') as f_obj:
    movies_database = json.load(f_obj)


def print_movies_from_list(movies_list):
    for movie in movies_list:
        print('\t' + movie)


def cut_movie_release_year_from(movie_release_date):
    # movie_release_date format: 'year-month-day'
    movie_release_year = int(movie_release_date.split('-')[0])
    return movie_release_year


def is_in_database(entered_movie_title):
    for movie in movies_database:
        if movie['title'].lower() == entered_movie_title.lower():
            return True
        else:
            return False


def get_movie_info_from_database(entered_movie_title):
    for movie in movies_database:
        if movie['title'].lower() == entered_movie_title.lower():
            return movie


def get_attr(entered_movie_title, searching_attr):
    for movie in movies_database:
        if movie[searching_attr] == entered_movie_title[searching_attr]:
            return movie[searching_attr]


entered_movie_title = input()

similar_title_movies = []
similar_genre_movies = []
similar_budget_movies = []
equal_release_year_movies = []


if is_in_database(entered_movie_title):
    entered_movie_info = get_movie_info_from_database(entered_movie_title)

    entered_movie_genres = get_attr(entered_movie_info, 'genres')
    entered_movie_budget = int(get_attr(entered_movie_info, 'budget'))
    entered_movie_release_date = get_attr(
        entered_movie_info, 'release_date')
    entered_movie_release_year = cut_movie_release_year_from(
        entered_movie_release_date)

for movie in movies_database:
    if entered_movie_title.lower() in movie['title'].lower():
        similar_title_movies.append(movie['title'])

    if is_in_database(entered_movie_title):
        if movie['budget'] in range(
           entered_movie_budget - 10000, entered_movie_budget + 10000):
            similar_budget_movies.append(movie['title'])

        movie_release_year = cut_movie_release_year_from(
            movie['release_date'])
        if entered_movie_release_year == movie_release_year:
            equal_release_year_movies.append(movie['title'])

        for entered_movie_genre in entered_movie_genres:
            for current_movie_genre in movie['genres']:
                if entered_movie_genre == current_movie_genre:
                    similar_genre_movies.append(movie['title'])


print('\nMovies with similar title:')
print_movies_from_list(similar_title_movies)

if is_in_database(entered_movie_title):
    print('\nMovies with similar budget:')
    print_movies_from_list(similar_budget_movies)

    print('\nMovies with the same release year:')
    print_movies_from_list(equal_release_year_movies)

    print('\nMovies with the same genres:')
    print_movies_from_list(similar_genre_movies)
