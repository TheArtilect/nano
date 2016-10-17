import webbrowser

class Movie():
    ''' This class is for storing information for movies '''

    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer= trailer


    def play_trailer(self):
        webbrowser.open(self.trailer)
        
