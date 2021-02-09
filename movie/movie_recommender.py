import requests
from bs4 import BeautifulSoup
import random

API_KEY = "067f1fe7a172d457785143a182dcf3ec"
API_ENDPOINT = "https://api.themoviedb.org/3/find/"


def movie_list_creator(f_year=0, t_year=0, movie_genre="", f_rating=5, t_rating=10):
    movie_list = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date={f_year}-01-01,{t_year}-12-31&user_rating={f_rating},{t_rating}&genres={movie_genre}&count=250 "
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.find_all(class_="lister-item-content")
    for card in cards:
        rating = card.find(class_="ratings-imdb-rating").getText().strip()
        title = card.find(class_="lister-item-header").getText().split("\n")[2]
        overview = card.find_all("p")[1].getText().strip()
        release_date = card.find(class_="lister-item-year").getText()
        try:
            duration = card.find(class_="runtime").getText().split()[0]
        except AttributeError:
            duration = "Not Found"
        try:
            genre = card.find(class_="genre").getText().strip()
        except AttributeError:
            genre = "Not Found"
        id_obj = card.find("span", class_="userRatingValue")
        imdb_id = id_obj.get("data-tconst")
        movie = {"imdb_id": imdb_id, "title": title,
                 "rating": rating, "runtime": duration, "overview": overview,
                 "release_date": release_date, "genre": genre}
        movie_list.append(movie)
    return movie_list


movie_list = movie_list_creator()


# Find Trailer and poster for the random movie
def poster_finder(movie):
    URL = f"https://api.themoviedb.org/3/find/{movie['imdb_id']}?" \
          f"api_key={API_KEY}&language=en-US&external_source=imdb_id"
    try:
        poster_link = "https://image.tmdb.org/t/p/w500/" + requests.get(URL).json()["movie_results"][0]["poster_path"]
    except IndexError:
        poster_link = 'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/fb3ef66312333.5691dd2253378.jpg'
    except TypeError:
        poster_link = 'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/fb3ef66312333.5691dd2253378.jpg'
    return poster_link


def trailer_finder(movie):
    trailer_finding_url = f"http://api.themoviedb.org/3/movie/{movie['imdb_id']}/videos?api_key={API_KEY}"
    response = requests.get(trailer_finding_url)
    try:
        yt_key = response.json()['results'][0]['key']
    except IndexError:
        yt_key = None
    except KeyError:
        yt_key = None
    return yt_key


def randomizer(lst):
    a = random.randint(0, len(lst)-6)
    b = a + 6
    return a, b
