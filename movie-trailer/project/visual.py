import webbrowser

from video import Video


class Movie(Video):
    ''' This class is for storing information for movies, a child of video '''

    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer= trailer


    #def play_trailer(self):
    #    webbrowser.open(self.trailer)


class Show(Video):
    ''' This class if for storing information for my favorite TV shows, a child of video '''

    def __init__(self, title, storyline, poster, trailer, seasons):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer
        self.seasons = seasons
