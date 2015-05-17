import webbrowser

class Movie:
    #This provides documentation about the class "Movie"
    """ This class provides a way to store movie related information """
      
    #Initializing and creating space in memory for what we are about to create
    #"self" is the object or instance being created
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

