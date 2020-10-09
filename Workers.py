#name = Ashwin
#date = 10/6/20

from Athlete import *


class Worker(Athlete):
    def __init__(self, world,x=2,y=2,d=east,b=0):
        Athlete.__init__(self, world, 2, 2, east, 0)
        
     def turnToTheNorth(self):
         while not self.facingNorth():
            self.turnRight()
     def harvest(self):
         
