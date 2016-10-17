import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


avatar = media.Movie("Avatar",
                    "A marine on an alien planet.",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "http://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)

#avatar.show_trailer()

fear = media.Movie("Fear and Loathing in Las Vegas",
                    "A journalist and his lawyer embark on an existentialist journey in the desert City of Las Vegas and wreak havoc.",
                    "https://upload.wikimedia.org/wikipedia/en/6/6f/FandlinLV.jpg",
                    "https://www.youtube.com/watch?v=vvrkNjaZX0A")

fear.show_trailer()
