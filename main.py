from microbit import *
from enum import *
import music
from modes import *
from keypad import *
from generatesinusoid import generate_sinusoid

LCD_I2C_ADDR=39
def reportResult(result):
    global l
    global currentlyDisplayed
    global problemInProgress
    global wantToDisplay
    if (result):
        #correct answer behavior
        #use a music function to celebrate
        speaker.off()
        music.POWER_UP
        wantToDisplay[1] =""
        wantToDisplay[0] = "Correct!"
        l.displayIfDiff(wantToDisplay, True)
    else:
        #incorrect result behavior
        wantToDisplay[0] = "Incorrect :("
        wantToDisplay[1] = ""
        l.displayIfDiff(wantToDisplay, True)
        #speaker plays incorrect ans tone
        speaker.off()
        music.POWER_DOWN
    sleep(2500)
    problemInProgress = False
class LCD1620():
    def __init__(self):
        self.buf = bytearray(1)
        self.BK = 0x08
        self.RS = 0x00
        self.E = 0x04
        self.setcmd(0x33)
        sleep(5)
        self.send(0x30)
        sleep(5)
        self.send(0x20)
        sleep(5)
        self.setcmd(0x28)
        self.setcmd(0x0C)
        self.setcmd(0x06)
        self.setcmd(0x01)
        self.version='1.0'

    def setReg(self, dat):
        self.buf[0] = dat
        i2c.write(LCD_I2C_ADDR, self.buf)
        sleep(1)

    def send(self, dat):
        d=dat&0xF0
        d|=self.BK
        d|=self.RS
        self.setReg(d)
        self.setReg(d|0x04)
        self.setReg(d)

    def setcmd(self, cmd):
        self.RS=0
        self.send(cmd)
        self.send(cmd<<4)

    def setdat(self, dat):
        self.RS=1
        self.send(dat)
        self.send(dat<<4)

    def clear(self):
        self.setcmd(1)

    def backlight(self, on):
        if on:
            self.BK=0x08
        else:
            self.BK=0
        self.setcmd(0)

    def on(self):
        self.setcmd(0x0C)

    def off(self):
        self.setcmd(0x08)

    def shl(self):
        self.setcmd(0x18)

    def shr(self):
        self.setcmd(0x1C)

    def char(self, ch, x=-1, y=0):
        if x>=0:
            a=0x80
            if y>0:
                a=0xC0
            a+=x
            self.setcmd(a)
        self.setdat(ch)

    def puts(self, s, x=0, y=0):
        if len(s)>0:
            self.char(ord(s[0]),x,y)
            for i in range(1, len(s)):
                self.char(ord(s[i]))
    def displayIfDiff(self, new, force=False):
        #print("display if diff called")
        global currentlyDisplayed
        if (currentlyDisplayed != new) or (force):
            #print("changing")
            currentlyDisplayed= new
            self.clear()
            self.puts(new[0])
            self.puts(new[1], y=1)
        
activeMode = mainMode.neither
def readOrientation():
    global activeMode
    #print("reading orientation")
    #sets the main operating mode according to the orientation
    if accelerometer.is_gesture('face up'):
        print("face up")
        activeMode= mainMode.math
    elif accelerometer.is_gesture('face down'):
        print("face down")
        activeMode = mainMode.music
    else:
        activeMode = mainMode.neither

display.off()

activeMathMode = mathMode.neither
currentlyDisplayed= ["",""]
enteredAnswer =""
wantToDisplay= ["",""]
#use currently displayed string to check to see if there needs to be
#any updates to the display? Need to think more about this


problemInProgress= False

answerEntered = False
orientationTicker = 0
displayStatus = False
#true for on false for off
l=LCD1620()

import random
from modes import mathMode
class mathProblem:
    def __init__(self, mode):
        self.mode= mode
        global problemInProgress
        problemInProgress = True
        if mode == mathMode.add:
            self.num1 = random.randint(1, 100)
            self.num2 = random.randint(1, 100)
            self.answer = self.num1+ self.num2
        elif mode == mathMode.sub:
            self.num1 = random.randint(2, 100)
            self.num2 = random.randint(1, 100)
            while self.num2 > self.num1:
                self.num2 = random.randint(1, 100)
            self.answer = self.num1 - self.num2
        elif mode == mathMode.mult:
            self.num1 = random.randint(1, 12)
            self.num2 = random.randint(1, 12)
            self.answer = self.num1 * self.num2
        elif mode == mathMode.div:
            self.num1 = random.randint(1, 100)
            self.num2 = random.randint(1, 100)
            while ((self.num1 % self.num2)!=0):
                self.num1 = random.randint(1, 100)
                self.num2 = random.randint(1, 100)
            self.answer = self.num1 / self.num2
      
    def displayProblem(self):
        global l
        global problemInProgress
        operatorString = ""
        outputString = ""
        #this will display the problem prompt on the LCD
        if self.mode == mathMode.mult:
            operatorString = "*"
        elif self.mode == mathMode.add:
            operatorString= "+"
        elif self.mode == mathMode.sub:
            operatorString= "-"
        elif self.mode == mathMode.div:
            operatorString = "/"
        outputString += str(self.num1) + operatorString + str(self.num2) + "=?"
        #includes a new line escape sequence so that the answer appears on the lower level
        problemInProgress = True
        global wantToDisplay
        wantToDisplay[0] = outputString
        wantToDisplay[1] = ""
        #print(outputString)
        #print(currentlyDisplayed)
        #print(wantToDisplay)
        l.displayIfDiff(wantToDisplay, True)
        sleep(150)
        
    def checkAnswer(self, userAnswer):
        if self.answer == int(userAnswer):
            return True
        else:
            return False
        
goBack = False        

#accelerometer.set_range(1)

while True:
    orientationTicker +=1
    if orientationTicker == 10:
        orientationTicker = 0
        readOrientation()
        #will only periodically check orientation
    if activeMode == mainMode.math:
        #perform math function
        #set music indicator light off
        if (not(displayStatus)):
            l.on
            l.backlight(True)
            displayStatus = True
        while problemInProgress:
            while(answerEntered != True):
                sleep(160)
                keypadOutput = keypadListen()
                if orientationTicker == 10:
                    readOrientation()
                    orientationTicker = 0
                    if mainMode != mainMode.math:
                        break
                #if keypadOutput != -1:
                    #print (keypadOutput)
                if keypadOutput == -1:
                    continue
                elif (keypadOutput == 12):
                    answerEntered = True
                elif (keypadOutput == 10):
                    problemInProgress = False
                    activeMathMode = mathMode.neither
                    goBack= True
                    break
                
                else:
                    if (keypadOutput == 11):
                        keypadOutput = 0
                    enteredAnswer += str(keypadOutput)
                    wantToDisplay[1] += str(keypadOutput)
                    l.displayIfDiff(wantToDisplay, True)
                #if enterpressed, answerEntered = True
                if answerEntered:
                    reportResult(currMathProblem.checkAnswer(enteredAnswer))
                    problemInProgress = False
            #if enter is pressed, set answerEntered flag to true
            #won't recreate a problem
            
        else:
            if activeMathMode == mathMode.neither:
                wantToDisplay[0] = "Select a mode:"
                wantToDisplay[1] = "1)+ 2)- 3)X 4)/"
                if (goBack):
                    l.displayIfDiff(wantToDisplay, True)
                l.displayIfDiff(wantToDisplay)
                subCounter = 10 #for reading orientation
                garbage = keypadListen()
                garbage = keypadListen()
                garbage = keypadListen()
                #for some reason, the microbit reads in a couple garbage values before it is ready to actually listen
                while activeMathMode == mathMode.neither:
                    subCounter -= 1
                    if subCounter == 0:
                        subCounter = 10
                        readOrientation()
                        if activeMode != mainMode.math:
                            break
                    selectedMode = keypadListen()
                    if selectedMode == 1:
                        activeMathMode = mathMode.add
                    elif selectedMode == 2:
                        activeMathMode = mathMode.sub
                    elif selectedMode == 3:
                        activeMathMode = mathMode.mult
                    elif selectedMode == 4:
                        activeMathMode = mathMode.div
                    #think about while loops, they prevent 
                    #orientation mode from being changed
                    #wait for user to click a button
                    #need to check orientation
                    #if x pushbutton, activeMathMode = pushbutton
            
            currMathProblem= mathProblem(activeMathMode)
            currMathProblem.displayProblem()
            answerEntered = False
            enteredAnswer = ""
        #depending on lcd functionality, we'll see what to do next    
        #we'll need a function to listen to the numpad and display the input
        #resultReporter(currMathProblem.checkAnswer)
    if activeMode == mainMode.music:
        if (displayStatus):
            
            l.clear()
            l.off
            l.backlight(False)
            displayStatus = False
        problemInProgress = False
        #set music indicator light to on pin 16
        musicValue = pin1.read_analog()
        if musicValue > 2 and musicValue < 2.2:
            generate_sinusoid(261.63, 500)
        elif musicValue > 2.2 and musicValue < 2.3:
            generate_sinusoid(293.66, 500)
        elif musicValue > 2.3 and musicValue < 2.4:
            generate_sinusoid(329.63, 500)
        elif musicValue > 2.4 and musicValue < 2.54:
            generate_sinusoid(349.23, 500)
        elif musicValue > 2.54 and musicValue < 2.68:
            generate_sinusoid(392, 500)
        elif musicValue > 2.68 and musicValue < 2.8:
            generate_sinusoid(440, 500)
        elif musicValue > 2.8 and musicValue < 2.96:
            generate_sinusoid(493.88, 500)
        elif musicValue > 2.96:
            generate_sinusoid(523.25, 500)
        #read push buttons and call music function
        #print("Music Mode!")
    if activeMode == mainMode.neither:
        if (displayStatus):
            l.clear()
            l.off
            l.backlight(False)
            displayStatus = False
        problemInProgress = False
        
        #set music indicator light off
        sleep(500)
    
