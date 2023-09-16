from ringBell import *
import main
def reportResult(result):
    if result:
        #correct answer behavior
        #lcd says correct!
        ringBell();
    else:
        #incorrect result behavior
        print("wrong")
        #speaker plays incorrect ans tone
        #lcd says incorrect
    problemInProgress = False