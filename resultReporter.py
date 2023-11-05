import main
import music
from microbit import *
def reportResult(result):
    if (result):
        #correct answer behavior
        #use a music function to celebrate
        speaker.off()
        music.POWER_UP
        main.l.displayIfDiff(["Correct!"])
    else:
        #incorrect result behavior
        main.l.displayIfDiff(["Incorrect :("])
        #speaker plays incorrect ans tone
        speaker.off()
        music.POWER_DOWN
    sleep(3200)
        
    main.problemInProgress = False
