from microbit import *
from enum import enum
from mathClass import *
from readOrientation import *
class mainMode(enum):
    neither = 0
    music = 1
    math = 2
class mathMode (enum):
    neither = 0
    add = 1
    sub = 2
    mult = 3
    div = 4
activeMode = mainMode.neither
activeMathMode = mathMode.neither

problemInProgress= False

while True:
    readOrientation()
    if activeMode == mainMode.math:
        #listen to mode select pushbuttons
        #We'll need to decide if we want the user to be able to change the mode
        #while 'in the middle' of an existing problem
        #perform math function
        #set music indicator light off
        if problemInProgress:
            #won't recreate a problem
            print("waiting for user input")
        else:
            currMathProblem= mathProblem(activeMathMode)
            currMathProblem.displayProblem()
        #depending on lcd functionality, we'll see what to do next    
        #we'll need a function to listen to the numpad and display the input
        #resultReporter(currMathProblem.checkAnswer)
    if activeMode == mainMode.music:
        #set music indicator light to on
        #read push buttons and call music function
        print("Music Mode!")
    if activeMode == mainMode.neither:
        #set music indicator light off
        sleep(1000)
    
