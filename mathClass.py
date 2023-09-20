import random
from main import mathMode
import main
class mathProblem:
    def __init__(self, mode):
        if mode == mathMode.add:
            self.num1 = random.randint(1, 100)
            self.num2 = random.randint(1, 100)
            self.answer = self.num1+ self.num2
        if mode == mathMode.sub:
            self.num1 = random.randint(2, 100)
            self.num2 = random.randint(1, 100)
            while self.num2 > self.num1:
                self.num2 = random.randint(1, 100)
            self.answer = self.num1 - self.num2
        if mode == mathMode.mult:
            self.num1 = random.randint(1, 12)
            self.num2 = random.randint(1, 12)
            self.answer = self.num1 * self.num2
        if mode == mathMode.div:
            self.num1 = random.randint(1, 100)
            self.num2 = random.randint(1, 100)
            while ((self.num1 % self.num2)!=0):
                self.num1 = random.randint(1, 100)
                self.num2 = random.randint(1, 100)
            self.answer = self.num1 / self.num2
      
    def displayProblem(self):
        print("display problem")
        #this will display the problem prompt on the LCD
        problemInProgress = True
    def checkAnswer(self, userAnswer):
        if self.answer == userAnswer:
            return True
        else:
            return False
    
   
        
        
    
   
