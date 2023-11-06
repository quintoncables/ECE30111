import music
from microbit import *
def music(pushbutton):
    speaker.off()
    if pushbutton == 1:
        #analog write pin 0
        music.pitch(261)
        sleep(300) #tone will play even when sleeping
        music.stop()
        #play first frequency
        print("playing first freq")
    elif pushbutton== 2:
        #play second frequency
        music.pitch(293)
        sleep(300)
        music.stop()
        print("playing second freq")
    elif pushbutton== 3:
        #play third frequency
        music.pitch(329)
        sleep(300)
        music.stop()
        print("playing third freq")
    elif pushbutton == 4:
        #play fourth frequency
        music.pitch(349)
        sleep(300)
        music.stop()
        print("playing fourth freq")
    elif pushbutton == 5:
        music.pitch(392)
        sleep(300)
        music.stop()
        #play fith frequency
        print("playing fith freq")
    elif pushbutton == 6:
        music.pitch(440)
        sleep(300)
        music.stop()
        #play sixth frequency
        print("playing sixth freq")
    elif pushbutton == 7:
        music.pitch(494)
        sleep(300)
        music.stop()
        #play seventh frequency
        print("playing seventh freq")
    elif pushbutton == 8:
        music.pitch(523)
        sleep(300)
        music.stop()
        #play eighth frequency
        print("playing eigth freq")
