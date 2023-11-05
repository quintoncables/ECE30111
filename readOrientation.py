from modes import  *
#from constants import *
from microbit import sleep
import main
from microbit import accelerometer
def readOrientation():
    #sets the main operating mode according to the orientation
    if accelerometer.is_gesture('face up'):
        #print("face up")
        main.activeMode= mainMode.math
    elif accelerometer.is_gesture('face down'):
        #print("face down")
        main.activeMode = mainMode.music
    else:
        main.activeMode = mainMode.neither

    
