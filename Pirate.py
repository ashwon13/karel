#name:Ashwin Pulla
#date:10/3/2020

from Athlete import *

class Pirate(Athlete):
    def __init__(self, world):
        Athlete.__init__(self, world, 1, 1, east, 0)
        
       
    def approachPile(self):
        while not self.nextToABeeper():
            self.move()
       
 
    def numOfBeepersInPile(self):
        
        count =0
        while self.nextToABeeper():
            self.pickBeeper()
            count=count+1
        
        return count 
        print count
        
 
    def turnAppropriately(self, beepers):
        
        if beepers == 1:
            self.turnLeft()
           
        elif beepers == 2:
            self.turnAround()
            
        elif beepers == 3:
            self.turnRight()
            
       
        
        
        



     
         
        
      
                      
        
        

