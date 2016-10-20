import fresh
from movie_search import get_movie
from movie_search import get_show


#  movies
fear = get_movie("Fear and loathing in las vegas", "https://www.youtube.com/watch?v=vvrkNjaZX0A")

goodfellas = get_movie("Goodfellas", "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

loop = get_movie("In The Loop", "https://www.youtube.com/watch?v=_VDc7-YH1LA")


terminator = get_movie("Terminator 2", "https://www.youtube.com/watch?v=7QXDPzx71jQ")

predator = get_movie("Predator", "https://www.youtube.com/watch?v=K9AT3tQGbIk")

godfather = get_movie("The Godfather", "https://www.youtube.com/watch?v=oAfWMr26KQk")

outrage = get_movie("Outrage", "https://www.youtube.com/watch?v=3Fj3htxRRHM")

aliens = get_movie("Aliens", "https://www.youtube.com/watch?v=zNE0dlHcmgA")

stargate = get_movie("Stargate", "https://www.youtube.com/watch?v=_mucMCddPy0")

big = get_movie("Big Trouble in Little China", "https://www.youtube.com/watch?v=592EiTD2Hgo")

memories = get_movie("Memories of Murder", "https://www.youtube.com/watch?v=NtOutxGJK5o")

chaser = get_movie("The Chaser", "https://www.youtube.com/watch?v=ai0GambXj-s")

yellow = get_movie("The Yellow Sea", "https://www.youtube.com/watch?v=YoyKIBiCb7Y")

devil = get_movie("I Saw The Devil", "https://www.youtube.com/watch?v=xwWgp1bqVwE")

waking = get_movie("Waking Life", "https://www.youtube.com/watch?v=SbPgprcMtjo")

event = get_movie("Event Horizon", "https://www.youtube.com/watch?v=OVlnER8SxfQ")

slc = get_movie("SLC Punk","https://www.youtube.com/watch?v=DILdeHgWF-U")

sunshine = get_movie("Eternal Sunshine of the Spotless Mind", "https://www.youtube.com/watch?v=hj7Wgd_Yn94")

tenenbaums = get_movie("The Royal Tenenbaums", "https://www.youtube.com/watch?v=lmOWfJXQzP8")

assassins = get_movie("13 Assassins","https://www.youtube.com/watch?v=NgPC74-Tde8")

# shows

breaking = get_show("Breaking Bad", "https://www.youtube.com/watch?v=XZ8daibM3AE")

venture = get_show("The Venture Bros.", "https://www.youtube.com/watch?v=ctlC0x2eeww")

sunny = get_show("It's Always Sunny in Philadelphia", "https://www.youtube.com/watch?v=XgAKMICbha0")

zrock = get_show("Z Rock", "https://www.youtube.com/watch?v=GCSUknJzzBw")

wire = get_show("The Wire", "https://www.youtube.com/watch?v=YN0rYQdEmXw")

walking = get_show("The Walking Dead", "https://www.youtube.com/watch?v=sfAc2U20uyg")





movies = [goodfellas, fear, big, assassins, yellow, memories, loop, tenenbaums,
            slc, terminator, predator, aliens, outrage, stargate,
             sunshine]

shows = [venture, sunny, breaking, zrock, wire, walking]

recommend = [devil, event, chaser]

fresh.open_movies_page(movies, shows, recommend)
