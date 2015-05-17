import fresh_tomatoes
import media


#This section is used to initialize the values in the Movie Class in the Media Module for each movie

toy_story = media.Movie("Toy Story",
                        "A story of a body and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=_Tkc5pQp_JE") 


prometheus = media.Movie("Prometheus",
                             "Following clues to the origin of mankind a team journey across the universe and find a structure on a distant planet containing a monolithic statue of a humanoid head and stone cylinders of alien blood but they soon find they are not alone.",
                             "http://ewinsidemovies.files.wordpress.com/2011/12/prometheus_810.jpg",
                             "https://www.youtube.com/watch?v=nmJOO6D5RvA")


matrix = media.Movie("Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                     "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")


mad_max_fury_road = media.Movie("Mad Max Fury Road",
                                "In a stark desert landscape where humanity is broken, two rebels just might be able to restore order: Max, a man of action and of few words, and Furiosa, a woman of action who is looking to make it back to her childhood homeland.",
                                "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSY9szIPbtk1-hwxdEVRJIHT_pgYGNnFkFSWsCjlKFGP3Pu77Oo",
                                "https://www.youtube.com/watch?v=YWNWi-ZWL3c")


whiplash = media.Movie("Whiplash",
                           "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
                           "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSyLORvKKvCi7-vy8vwi2s8F62aG7D36H15A8rOVfP2d7koyA9I",
                           "https://www.youtube.com/watch?v=tYkuvB2f5XU")


#"import fresh_tomatoes" allows to turn this code into a movie website by using function "open_movies_page"  
#The "open_movies_page" function takes a list or array of movies, then outputs or creates and opens
#an html webpage or website that shows those movies
movies = [toy_story, avatar, prometheus, matrix, mad_max_fury_road, whiplash]
fresh_tomatoes.open_movies_page(movies)




