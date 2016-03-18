import media
import fresh_tomatoes

''' 
This python file includes a movie list that contains all of my favorite
moive. Those movie are described based on the Movie class in the
media.py.
On the other hand, at the end of this python file, the function named
open_movies_page from fresh_tomatoes has been called to generate a 
webpage that display the movies from this list, and play the movie 
trailer with embedded youtube player on this webpage
'''
# Edit the movies basic information
toy_story = media.Movie(
	"Toy Story", 
	"A story of a boy and his toys that come to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc",
	"John Lasseter")

avatar = media.Movie(
	"Avatar",
 	"A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-\
	Poster.jpg",
	"https://www.youtube.com/watch?v=_i2RCBa3l-g",
	"James Cameron")

prometheus = media.Movie(
	"Prometheus",
	"The origin of the Alien",
	"https://upload.wikimedia.org/wikipedia/en/thumb/a/a3/\
	Prometheusposterfixed.jpg/220px-Prometheusposterfixed.jpg",
	"www.youtube.com/watch?v=im7eEg5-GDo",
	"Ridley Scott")

titanic = media.Movie(
	"Titanic",
	"A love story on this unsinkable ship",
	"https://upload.wikimedia.org/wikipedia/en/thumb/2/22/\
	Titanic_poster.jpg/220px-Titanic_poster.jpg",
	"www.youtube.com/watch?v=2e-eXJ6HgkQ",
	"James Cameron")

xi_you = media.Movie(
	"Journey To The West Conquering The Demon",
	"A very popular traditional story in China",
	"https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/\
	JourneytotheWestConqueringtheDemons.jpg/\
	220px-JourneytotheWestConqueringtheDemons.jpg",
	"https://www.youtube.com/watch?v=aelriSQLqkc",
	"Stephen Chow")

world_war_z = media.Movie(
	"World War Z",
	"An UN agent on the way to save humanity by finding the cure of zombie.",
	"https://upload.wikimedia.org/wikipedia/en/7/76/World_War_Z_book_cover.jpg",
	"https://www.youtube.com/watch?v=HcwTxRuq-uk",
	"Marc Forster")

# Add the movies to the movies list
movies= [toy_story, avatar, prometheus, titanic, xi_you, world_war_z]

# Generate the movie trailer website based on the movie list above
fresh_tomatoes.open_movies_page(movies)
