# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import fresh_tomatoes
import media
# import fresh_tomatoes

wall_e = media.Movie("Wall-E",
						"A robot left behind on Earth falls in love with an unexpected visitor.",
						"https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
						"https://youtu.be/8-_9n5DtKOc?t")

avatar = media.Movie("Avatar",
					"A marine on an alien planet.",
					"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					"https://youtu.be/5PSNL1qE6VY?t")

inception = media.Movie("Inception",
						"A team of people go into a man's dream to plant an idea.",
						"https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
						"https://youtu.be/8hP9D6kZseM?t")

django = media.Movie("Django Unchained",
					"A slave and a bounty hunter team up to rescue the slave's wife.",
					"https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
					"https://youtu.be/eUdM9vrCbow?t")

jack_reacher = media.Movie("Jack Reacher",
							"An ex-military cop is summoned by a murder's prime suspect.",
							"https://upload.wikimedia.org/wikipedia/en/d/d1/Jack_Reacher_poster.jpg",
							"https://youtu.be/kK7y8Ou0VvM?t")

edge_of_tomorrow = media.Movie("Edge Of Tomorrow",
								"Ground hog day movie set on Earth in the middle of a human v. alien war.",
								"https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
								"https://www.youtube.com/watch?v=yUmSVcttXnI")

movies = [wall_e, avatar, inception, django, jack_reacher, edge_of_tomorrow]

fresh_tomatoes.open_movies_page

fresh_tomatoes.open_movies_page(movies)
