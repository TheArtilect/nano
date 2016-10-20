import requests
import visual




def get_movie(movie, youtube):
    url = "https://www.omdbapi.com/?t=" + movie + "&plot=short&r=json"
    movie_info = requests.get(url).json()
    title = movie_info[u'Title']
    plot = movie_info[u'Plot']
    poster = movie_info[u'Poster']
    return visual.Movie(title, plot, poster, youtube)
