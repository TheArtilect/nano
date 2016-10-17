import webbrowser
import time

breaktime = 2 * 60 * 60

print ("This program started on" + time.ctime())
for x in range(0, 3):
    time.sleep(breaktime)
    webbrowser.open("https://www.youtube.com/watch?v=efFo-Clq844")
