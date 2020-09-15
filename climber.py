from karel import *
from Athlete import Athlete
class Climber(Athlete):
    def __init__(self,world,x=1,y=1, direction=north, beepers=1):
        Athlete.__init__(self,world,x,y,direction,beepers)

    def climbUpRight(self):
        Athlete.move()
        Athlete.turnRight()


    def climbDownRight(self):
        Athlete.move()
        Athlete.turnRight()    
        
        
    def climbUpLeft(self):
        Athlete.move()
        Athlete.turnLeft()
        
        
    def climbDownLeft(self):
        Athlete.move()
        Athlete.turnLeft() 
