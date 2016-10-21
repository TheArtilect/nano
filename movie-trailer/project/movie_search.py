import requests
import visual


# Using OMBDb API for movie and show info, no api key needed

#  Generate movie object
def get_movie(movie, youtube):
    url = "https://www.omdbapi.com/?t=" + movie + "&plot=short&r=json"
    movie_info = requests.get(url).json()
    title = movie_info[u'Title']
    plot = movie_info[u'Plot']
    poster = movie_info[u'Poster']
    return visual.Movie(title, plot, poster, youtube)


# Generate show object
def get_show(show, youtube):
        url = "https://www.omdbapi.com/?t=" + show + "&plot=short&r=json"
        show_info = requests.get(url).json()
        title = show_info[u'Title']
        plot = show_info[u'Plot']
        poster = show_info[u'Poster']
        seasons = show_info[u'totalSeasons']
        return visual.Show(title, plot, poster, youtube, seasons)
