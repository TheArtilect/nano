import webbrowser


class Video():
    ''' This class is the parent class video

    Attributes:
        title (str):  Title of movie or show.
        storyline (str): Plot of movie or show.
        poster (str): Poster image of movie or show.
        trailer (str): Youtube link for the trailer of movie or show.
    '''
    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
