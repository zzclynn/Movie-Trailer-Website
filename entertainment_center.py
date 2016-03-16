import media
import fresh_tomatoes

# The movies list

toy_story = media.Movie("Toy Story", 
 			"A story of a boy and his toys that come to life",
			"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
		 	"A marine on an alien planet",
			"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
			"https://www.youtube.com/watch?v=_i2RCBa3l-g")

prometheus = media.Movie("Prometheus",
			"The origin of the Alien",
			"https://upload.wikimedia.org/wikipedia/en/thumb/a/a3/Prometheusposterfixed.jpg/220px-Prometheusposterfixed.jpg",
			"www.youtube.com/watch?v=im7eEg5-GDo")

titanic = media.Movie("Titanic",
			"A love story on this unsinkable ship",
			"https://upload.wikimedia.org/wikipedia/en/thumb/2/22/Titanic_poster.jpg/220px-Titanic_poster.jpg",
			"www.youtube.com/watch?v=2e-eXJ6HgkQ")

xi_you = media.Movie("Journey To The West Conquering The Demon",
			"A very popular traditional story in China",
			"https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/JourneytotheWestConqueringtheDemons.jpg/220px-JourneytotheWestConqueringtheDemons.jpg",
			"https://www.youtube.com/watch?v=aelriSQLqkc")

world_war_z = media.Movie("World War Z",
			"An UN agent on the way to save human by finding the care of zombie.",
			"https://upload.wikimedia.org/wikipedia/en/7/76/World_War_Z_book_cover.jpg",
			"https://www.youtube.com/watch?v=HcwTxRuq-uk")

movies= [toy_story,avatar,prometheus, titanic, xi_you, world_war_z]
fresh_tomatoes.open_movies_page(movies)
