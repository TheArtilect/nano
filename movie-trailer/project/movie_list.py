import fresh

import movie


fear = movie.Movie("Fear and Loathing in Las Vegas",
                    "A journalist and his lawyer embark on an existentialist journey in the desert City of Las Vegas and wreak havoc.",
                    "https://upload.wikimedia.org/wikipedia/en/6/6f/FandlinLV.jpg",
                    "https://www.youtube.com/watch?v=vvrkNjaZX0A")


goodfellas = movie.Movie("Goodfellas",
                        "Mafioso carve their own version of the American Dream.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/7/7b/Goodfellas.jpg/220px-Goodfellas.jpg",
                        "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

loop = movie.Movie("In The Loop",
                    "A revealing look inside the world of global politics and war.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/0/01/In_the_Loop_poster.jpg/220px-In_the_Loop_poster.jpg",
                    "https://www.youtube.com/watch?v=_VDc7-YH1LA")




professional = movie.Movie("The Professional",
                            "A hitman begins a friendship with an innocent girl.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Leon-poster.jpg/220px-Leon-poster.jpg",
                            "https://www.youtube.com/watch?v=aNQqoExfQsg")

terminator = movie.Movie("Terminator 2: Judgement Day",
                        "An android from the future protects the savior of the human race.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Terminator2poster.jpg/220px-Terminator2poster.jpg",
                        "https://www.youtube.com/watch?v=7QXDPzx71jQ")

predator = movie.Movie("Predator",
                        "An alien hunter stalks a military unit in the jungle",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/9/95/Predator_Movie.jpg/220px-Predator_Movie.jpg",
                        "https://www.youtube.com/watch?v=K9AT3tQGbIk")


godfather = movie.Movie("The Godfather",
                        "A master piece of cinema",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                        "https://www.youtube.com/watch?v=fB_8VCwXydM")


wonder = movie.Movie("Wonderboys",
                    "An author has a mid-life crisis.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/OriginalWBposter.jpg/220px-OriginalWBposter.jpg",
                    "https://www.youtube.com/watch?v=sveK_fhIqhs")


aliens = movie.Movie("Aliens",
                    "Space marines battle aliens.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Aliens_poster.jpg/220px-Aliens_poster.jpg",
                    "https://www.youtube.com/watch?v=zNE0dlHcmgA")





stargate = movie.Movie("Stargate",
                        "A team travels to an alien planet.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Stargateposter.jpg/220px-Stargateposter.jpg",
                        "https://www.youtube.com/watch?v=_mucMCddPy0")


'''
    breathless, i saw the devil, chaser, something of a murder, waking life, slc punk, eternal sunshine

    breaking bad, the walking dead, lost, vikings, venture brothers, it's always sunny, zrock, the wire,

'''

breaking = movie.Show("Breaking Bad",
                        "A high school chemistry teacher with terminal cancer turns to crime to provide for his family",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/6/61/Breaking_Bad_title_card.png/250px-Breaking_Bad_title_card.png",
                        "https://www.youtube.com/watch?v=XZ8daibM3AE",
                        "5",
                        "American Movie Classics")

venture = movie.Show("The Venture Bros.",
                        "A scientist and former boy adventurer, along with his sons and bodyguard tangle paths with supervillians.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/The_Venture_Bros_logo.svg/250px-The_Venture_Bros_logo.svg.png",
                        "https://www.youtube.com/watch?v=ctlC0x2eeww",
                        "6",
                        "Adult Swim")

sunny = movie.Show("It's Always Sunny in Philadelphia",
                        "Five friends who own a bar get into misadventures.",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/IASIPTC.png/250px-IASIPTC.png",
                        "https://www.youtube.com/watch?v=ctlC0x2eeww",
                        "11",
                        "FX")


movies = [goodfellas, stargate, terminator,
            predator, aliens,
            godfather]

shows = [venture, sunny, breaking]

recommend = [loop, professional, wonder]

fresh.open_movies_page(movies, shows, recommend)
