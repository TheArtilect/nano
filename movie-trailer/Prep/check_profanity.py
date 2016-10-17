import urllib

def read_text():
    quotes = open("/home/onyx/projects/nano/movie-trailer/movie_quotes.txt")
    contents = quotes.read()
    #print(contents)
    quotes.close()
    check_profanity(contents)


def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read()
    #print(output)
    connection.close()
    if 'true' in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")


read_text()
