#name = Ashwin
#date = 10/6/20

from Athlete import *
from pyKarel import *


class Harvester(Athlete):
   def __init__(self, world,x=2,y=2,d=east,b=0):
      Athlete.__init__(self, world, 2, 2, east, 0)
        
   def turnToTheNorth(self):
      while not self.facingNorth():
         self.turnRight()
   def doYourThing(self):
      while self.nextToABeeper():
         self.pickBeeper()
        
            
class Planter(Athlete):
   def __init__(self, world,x=2,y=2,d=east,b=infinity):
      Athlete.__init__(self, world, 2, 2, east, infinity)
       
def turnToTheNorth(self):
   while not self.facingNorth():
      self.turnRight()
        
         
def doYourThing(self):
   while not self.nextToABeeper():
      self.putBeeper()

     
         
