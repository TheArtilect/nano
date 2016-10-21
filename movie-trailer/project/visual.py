import webbrowser

from video import Video


class Movie(Video):
    ''' This class is for storing information for movies, a child of video

    Attributes:
        title (str):  Title of movie.
        storyline (str): Plot of movie.
        poster (str): Poster image of movie.
        trailer (str): Youtube link for the trailer of movie.


    '''



    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer= trailer


class Show(Video):
    ''' This class if for storing information for my favorite TV shows, a child of video

    Attributes:
        title (str):  Title of show.
        storyline (str): Plot of show.
        poster (str): Poster image of show.
        trailer (str): Youtube link for the trailer of show.
        seasons (str): The number of seasons of the show.

    '''

    def __init__(self, title, storyline, poster, trailer, seasons):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer
        self.seasons = seasons
