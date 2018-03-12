import json

if __name__ == '__main__':
    with open('movies_database.json') as f_obj:
        movies_database = json.load(f_obj)

    user_search_subtitle = input()

    for movie in movies_database:
        if user_search_subtitle.lower() in movie['title'].lower():
            print(movie['title'])
