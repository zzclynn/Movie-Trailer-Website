import webbrowser


class Movie:
	'''This is the Movie class that define the features to describe a movie'''

	def __init__(
			self,  movie_title, movie_storyline, 
			poster_image, trailer_youtube, director):
		'''This function construct movie objects'''
		self.title=movie_title
		self.storyline=movie_storyline
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_youtube
		self.director=director 

	def show_trailer(self):
		'''This function open the youtube url in browser'''
		webbrowser.open(self.trailer_youtube_url)
