import random
from main import mathMode
import main
class mathProblem:
    def __init__(self, mode):
        self.num1 = random.randint(1, 12)
        self.num2 = random.randint(1, 12)
        if mode == mathMode.add:
            self.answer = self.num1+ self.num2
        #write answer generating stuff later
    def displayProblem(self):
        print("display problem")
        #this will display the problem prompt on the LCD
        problemInProgress = True
    def checkAnswer(self, userAnswer):
        if self.answer == userAnswer:
            return True
        else:
            return False
        
        
    
   